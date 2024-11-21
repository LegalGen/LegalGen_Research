from openai.embeddings_utils import get_embedding

def generate_embeddings(text_segments):
    """
    Generate embedding vector for the legal agreement based on its text segments.
    Args:
        text_segments (list): List of text segments from the legal agreement.
    Returns:
        list: Overall embedding vector for the agreement (average of segment embeddings).
    """
    segment_embeddings = [get_embedding(segment, engine="text-embedding-ada-002") for segment in text_segments]

    agreement_embedding = [sum(x) / len(segment_embeddings) for x in zip(*segment_embeddings)]
    return agreement_embedding
