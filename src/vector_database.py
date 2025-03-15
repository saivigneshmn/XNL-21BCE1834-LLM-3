import faiss
import numpy as np

if __name__ == "__main__":
    combined_features = np.load("data/combined_features.npy")
    index = faiss.IndexFlatL2(combined_features.shape[1])
    index.add(combined_features)
    faiss.write_index(index, "data/faiss_index.idx")