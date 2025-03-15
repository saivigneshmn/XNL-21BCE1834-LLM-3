from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from gensim.models import Word2Vec
import numpy as np
import pandas as pd

def extract_text_features(data):
    vectorizer = TfidfVectorizer(max_features=100)
    tfidf_features = vectorizer.fit_transform(data["merchant"]).toarray()
    
    sentences = [merchant.split() for merchant in data["merchant"]]
    word2vec_model = Word2Vec(sentences, vector_size=50, window=5, min_count=1, workers=4)
    word2vec_features = np.array([np.mean([word2vec_model.wv[word] for word in merchant.split()], axis=0) 
                                 for merchant in data["merchant"]])
    
    return tfidf_features, word2vec_features

def extract_numerical_features(data):
    numerical_data = data[["amount", "age", "credit_score", "network_latency"]]
    pca = PCA(n_components=2)
    pca_features = pca.fit_transform(numerical_data)
    return pca_features

if __name__ == "__main__":
    transaction_data = pd.read_csv("data/transaction_data.csv")
    tfidf_features, word2vec_features = extract_text_features(transaction_data)
    pca_features = extract_numerical_features(transaction_data)
    combined_features = np.hstack((tfidf_features, word2vec_features, pca_features))
    np.save("data/combined_features.npy", combined_features)