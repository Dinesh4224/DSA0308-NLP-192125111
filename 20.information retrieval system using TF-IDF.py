from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample documents
documents = [
    "TF-IDF is a technique for information retrieval",
    "It is commonly used in search engines",
    "TF-IDF considers the frequency of words in a document and across documents",
    "The cosine similarity metric is often used to rank documents"
]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Get user query
query = input("Enter your query: ")

# Transform user query into TF-IDF vector
query_vector = vectorizer.transform([query])

# Calculate cosine similarity between query vector and document vectors
cosine_similarities = cosine_similarity(tfidf_matrix, query_vector)

# Get document indices sorted by relevance
sorted_indices = np.argsort(cosine_similarities, axis=0)[::-1].flatten()

# Print ranked documents
print("Ranked documents:")
for index in sorted_indices:
    print(f"Document {index + 1}: {documents[index]}")
