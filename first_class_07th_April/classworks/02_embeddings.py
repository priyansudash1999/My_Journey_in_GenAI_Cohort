import google.generativeai as genai
import os

# Replace with your actual API key
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

# Load the embedding model
embedding_model = genai.GenerativeModel('models/embedding-001')

# Sentence to embed
sentence_to_embed = "How can I get vector embeddings using the Gemini API?"

# Get the embedding
embedding_response = embedding_model.embed(sentence_to_embed)
embedding_vector = embedding_response.values

print(f"Embedding for '{sentence_to_embed}':")
print(embedding_vector)
print(f"Embedding dimensions: {len(embedding_vector)}")

# Example with multiple sentences
sentences_to_embed = ["Gemini is a powerful language model.", "Vector embeddings capture semantic meaning."]
embeddings_response = embedding_model.embed(sentences_to_embed)
embedding_vectors = embeddings_response.values

for i, sentence in enumerate(sentences_to_embed):
    print(f"\nEmbedding for '{sentence}':")
    print(embedding_vectors[i])
    print(f"Embedding dimensions: {len(embedding_vectors[i])}")