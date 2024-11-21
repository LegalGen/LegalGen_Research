def infer_ontology(concept_descriptions):
    prompt = f"""
    Based on the following extracted legal concepts, infer an ontology structure to represent the key logic of the legal agreement. 
    Format the output as:
    - Key: ...
      - Type: ...
      - Description: ...
      - Relations: ...
      - Constraints: ...
    Legal Concepts: {concept_descriptions}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in legal ontologies, specializing in defining structured concepts."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"].strip()

# Load extracted concepts from JSON file
with open("concepts.json", "r") as f:
    concept_descriptions = json.load(f)


ontology = infer_ontology(concept_descriptions)


with open("ontology.json", "w") as f:
    json.dump(ontology, f, indent=4)

print("Ontology inference complete. Results saved to ontology.json")
