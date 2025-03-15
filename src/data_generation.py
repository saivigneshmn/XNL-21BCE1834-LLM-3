from faker import Faker
import pandas as pd
import numpy as np
import random

def generate_transaction_data(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        transaction = {
            "user_id": fake.uuid4(),
            "age": random.randint(18, 80),
            "region": fake.country_code(),
            "credit_score": random.randint(300, 850),
            "timestamp": fake.date_time_this_year(),
            "amount": round(random.uniform(10.0, 10000.0), 2),
            "merchant": fake.company(),
            "ip": fake.ipv4(),
            "device_fingerprint": fake.uuid4(),
            "location": (fake.latitude(), fake.longitude()),
            "browser_info": fake.user_agent(),
            "network_latency": round(random.uniform(0.1, 5.0), 2),
            "time_of_day": fake.time(),
            "label": random.choices(["normal", "suspicious", "fraudulent"], weights=[0.85, 0.1, 0.05])[0]
        }
        data.append(transaction)
    return pd.DataFrame(data)

if __name__ == "__main__":
    num_records = 100000  # 1M records
    transaction_data = generate_transaction_data(num_records)
    transaction_data.to_csv("data/transaction_data.csv", index=False)