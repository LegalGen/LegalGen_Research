import numpy as np

def calculate_distance(embedding1, embedding2):
    """
    Compute the Euclidean distance between two embedding vectors.
    Args:
        embedding1 (list): First embedding vector.
        embedding2 (list): Second embedding vector.
    Returns:
        float: Euclidean distance between the two vectors.
    """
    return np.linalg.norm(np.array(embedding1) - np.array(embedding2))
