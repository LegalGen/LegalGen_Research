def find_closest_cluster(agreement_embedding, clusters):
    """
    Identify the cluster most similar to the legal agreement based on embeddings.
    Args:
        agreement_embedding (list): Embedding vector of the legal agreement.
        clusters (list): List of cluster data, each containing cluster_id and embedding.
    Returns:
        dict: Information about the closest cluster, including cluster_id and concept descriptions.
    """
    min_distance = float('inf')
    closest_cluster = None
    
    for cluster in clusters:
        distance = calculate_distance(agreement_embedding, cluster["embedding"])
        if distance < min_distance:
            min_distance = distance
            closest_cluster = cluster
    
    return {
        "cluster_id": closest_cluster["cluster_id"],
        "concept_descriptions": closest_cluster["concept_descriptions"]
    }
