from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("FraudDetection") \
        .getOrCreate()
    
    df = spark.read.csv("data/transaction_data.csv", header=True, inferSchema=True)
    df.show()