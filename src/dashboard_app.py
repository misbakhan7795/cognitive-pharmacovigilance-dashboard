import gradio as gr

from pipeline_nlp import get_drug_stats
from sentiment_pipeline import analyze_sentiment
from retrieve_faers import search_faers


def analyze_drug(drug):

    stats = get_drug_stats(drug)

    overview = f"""
Drug: {drug}

Review Count: {stats['review_count']}

Average Rating: {stats['avg_rating']}
"""

    # Sentiment Analysis
    sentiment_result = analyze_sentiment(
        stats["sample_review"]
    )

    sentiment = f"""
Label: {sentiment_result['label']}

Confidence: {round(sentiment_result['score'], 3)}
"""

    # FDA Retrieval
    results = search_faers(
        f"{drug} adverse event"
    )

    fda = "\n\n".join(results[:5])

    # AI Analysis Placeholder
    analysis = """
Gemini reasoning coming next
"""

    return (
        overview,
        sentiment,
        fda,
        analysis
    )


with gr.Blocks(title="PharmaGuard AI Core") as demo:

    gr.Markdown("# 🛡️ PharmaGuard AI Core")

    drug = gr.Textbox(
        label="Drug Name",
        placeholder="Enter a drug name (e.g. ibuprofen)"
    )

    run_btn = gr.Button("Analyze")

    with gr.Tab("Overview"):
        overview = gr.Textbox(lines=10)

    with gr.Tab("Patient Sentiment"):
        sentiment = gr.Textbox(lines=10)

    with gr.Tab("FDA Signals"):
        fda = gr.Textbox(lines=10)

    with gr.Tab("AI Analysis"):
        analysis = gr.Textbox(lines=10)

    run_btn.click(
        fn=analyze_drug,
        inputs=drug,
        outputs=[
            overview,
            sentiment,
            fda,
            analysis
        ]
    )

demo.launch(
    share=False,
    inbrowser=True
)