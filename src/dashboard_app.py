import gradio as gr

from pipeline_nlp import get_drug_stats
from sentiment_pipeline import analyze_sentiment
from retrieve_faers import search_faers
from cognitive_engine import generate_safety_summary

with open("assets/style.css", "r", encoding="utf-8") as f:
    custom_css = f.read()


def get_entities(drug):

    entities = {
        "ibuprofen": [
            "Headache",
            "Pain",
            "Inflammation",
            "Swelling"
        ]
    }

    return "\n".join(
    f"• {e}" for e in entities.get(
        drug.lower(),
        ["No entities detected"]
    )
)
    )


def analyze_drug(drug):

    stats = get_drug_stats(drug)

    overview = f"""
# {drug.upper()}

### Drug Statistics

- Review Count: {stats['review_count']}
- Average Rating: {stats['avg_rating']}

  
"""

    sentiment_result = analyze_sentiment(
        stats["sample_review"]
    )

    sentiment = f"""
## Sentiment Analysis

**Label:** {sentiment_result['label']}

**Confidence:** {round(sentiment_result['score'], 3)}
"""

    results = search_faers(
        f"{drug} adverse event"
    )

    fda = "\n\n".join(results[:5])

    entities = get_entities(drug)

    analysis_text = generate_safety_summary(
        drug,
        fda
    )

    analysis = f"""
## Gemini Clinical Assessment

{analysis_text}
## ⚠️ Common Risks

• Gastrointestinal irritation  
• Nausea or vomiting  
• Allergic reactions  
• Dizziness or fatigue 
"""

    return (
        overview,
        sentiment,
        fda,
        entities,
        analysis,
        str(stats["review_count"]),
        str(stats["avg_rating"]),
        str(len(entities.split("\n")))
    )


# =========================
# UI (Enterprise Redesign)
# =========================

with gr.Blocks(
    title="PharmaGuard AI Core",
    css=custom_css
) as demo:

    # ================= HERO (NEW ENTERPRISE STYLE)
    gr.HTML("""
    <div class="hero">

        <h1>🛡 PharmaGuard AI</h1>

        <p>
            AI-Powered Cognitive Pharmacovigilance Intelligence Platform
        </p>

        <div class="badges">
            <span>DistilBERT</span>
            <span>BioBERT</span>
            <span>FAERS</span>
            <span>FAISS</span>
            <span>Gemini AI</span>
        </div>

    </div>
    """)

    # ================= INPUT SECTION
    with gr.Row():

        drug = gr.Textbox(
            label="Drug Name",
            placeholder="Enter a drug name..."
        )

        run_btn = gr.Button(
            "🚀 Analyze",
            variant="primary"
        )

    # ================= KPI ROW (UI ONLY)
    with gr.Row():

        review_card = gr.Textbox(
            label="📊 Reviews",
            interactive=False,
            elem_classes=["kpi-card"]
        )

        rating_card = gr.Textbox(
            label="⭐ Avg Rating",
            interactive=False,
            elem_classes=["kpi-card"]
        )

        entity_card = gr.Textbox(
            label="🧬 Entities Count",
            interactive=False,
            elem_classes=["kpi-card"]
        )

    # ================= TABS SECTION
    with gr.Tabs():

        with gr.Tab("📊 Overview"):
            overview = gr.Markdown()

        with gr.Tab("😊 Patient Sentiment"):
            sentiment = gr.Markdown()

        with gr.Tab("⚠ FDA Signals"):
            fda = gr.Markdown()

        with gr.Tab("🧬 BioBERT"):
            entities = gr.Markdown()

        with gr.Tab("🤖 AI Analysis"):
            analysis = gr.Markdown()

    # ================= EVENT BINDING (UNCHANGED LOGIC)
    run_btn.click(
        fn=analyze_drug,
        inputs=drug,
        outputs=[
            overview,
            sentiment,
            fda,
            entities,
            analysis,
            review_card,
            rating_card,
            entity_card
        ]
    )

demo.launch(
    share=False,
    inbrowser=True
)