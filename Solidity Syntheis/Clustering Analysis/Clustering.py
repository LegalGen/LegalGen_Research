from sklearn.cluster import KMeans

# Perform K-Means clustering
n_clusters = 5  
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
labels = kmeans.fit_predict(embeddings)

for i, label in enumerate(labels):
    print(f"Legal Text {i} belongs to Cluster {label}")
