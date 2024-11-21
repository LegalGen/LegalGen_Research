from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=42)
reduced_embeddings = tsne.fit_transform(embeddings)

# Plot the clustering results
plt.figure(figsize=(8, 8))
for i in range(n_clusters):
    cluster_points = reduced_embeddings[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f"Cluster {i}")

plt.title("t-SNE Visualization of Clusters")
plt.legend()
plt.show()
