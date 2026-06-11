from cognitive_engine import generate_safety_summary

print(
    generate_safety_summary(
        "Ibuprofen",
        "Mostly positive reviews",
        [
            "IBUPROFEN adverse event Headache",
            "IBUPROFEN adverse event Nausea",
            "IBUPROFEN adverse event Dizziness"
        ]
    )
)