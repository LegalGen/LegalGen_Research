import openai
import numpy as np

# Set OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Example legal agreement texts
legal_texts = [
    "This is the first legal agreement...",
    "The second legal agreement is about...",
    "Another example of legal agreements..."
]

# Generate text embeddings
def generate_embeddings(texts):
    embeddings = []
    for text in texts:
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )
        embeddings.append(response['data'][0]['embedding'])
    return np.array(embeddings)

embeddings = generate_embeddings(legal_texts)
