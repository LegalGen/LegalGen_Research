from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Calculate Sum of Squared Errors (SSE)
def calculate_sse(embeddings, max_clusters=10):
    sse = []
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(embeddings)
        sse.append(kmeans.inertia_)
    return sse

sse = calculate_sse(embeddings)

# Plot Elbow Method curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), sse, marker='o')
plt.title("Elbow Method for Optimal Clusters")
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()
