import openai
import json

openai.api_key = "your_openai_api_key"

def extract_concepts(text_segment):
    prompt = f"""
    Extract key legal concepts from the following text and format the output as:
    - Parties and Roles: ...
    - Payment Terms: ...
    - Termination Conditions: ...
    Text: {text_segment}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a legal assistant specialized in analyzing legal agreements."},
            {"role": "user", "content": prompt}
        ]
    )
    # Extract the content from the response
    return response["choices"][0]["message"]["content"].strip()

def process_segments(text_segments):
    concepts = []
    for segment in text_segments:
        extracted_concepts = extract_concepts(segment)
        concepts.append(extracted_concepts)
    return concepts


text_segments = [
    "This Employment Agreement is between the Company and the Employee...",
    "In case of termination without cause, a lump-sum of the annual salary is paid..."
]


concept_descriptions = process_segments(text_segments)

# Save the concepts as a JSON file
with open("concepts.json", "w") as f:
    json.dump(concept_descriptions, f, indent=4)

print("Concept extraction complete. Results saved to concepts.json")
