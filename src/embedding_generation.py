from transformers import AutoTokenizer, AutoModel
import numpy as np

def generate_embeddings(texts):
    tokenizer = AutoTokenizer.from_pretrained("./models/yiyanghkust/finbert-tone")
    model = AutoModel.from_pretrained("./models/yiyanghkust/finbert-tone")
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    return embeddings

if __name__ == "__main__":
    texts = ["Sample transaction description"]
    embeddings = generate_embeddings(texts)
    np.save("data/merchant_embeddings.npy", embeddings)