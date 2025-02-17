from confluent_kafka import Consumer 
from pymongo import MongoClient 
from pymongo.server_api import ServerApi 
import json
from datetime import datetime
import logging

# Kafka configuration settings
kafka_config = { 
    'bootstrap.servers': 'pkc-619z3.us-east1.gcp.confluent.cloud:9092', 
    'security.protocol': 'SASL_SSL', 
    'sasl.mechanisms': 'PLAIN', 
    'sasl.username': 'UMZEHTYDMU4CXERS', 
    'sasl.password': 'rJzlHQFmTzMqklVMBkBOJzvTsUFQ0dy7hwse23Yr/VKj//NRhJMOT21I3zTFGY5lH', 
    'group.id': 'sentiment_analysis_group', 
    'auto.offset.reset': 'earliest'
}

# Kafka topic name
kafka_topic = "customer_click_data"

# MongoDB connection URI
mongo_uri = "mongodb+srv://amit1234:mfynycf0j812342@amit.yygfj.mongodb.net/?retryWrites=true&w=majority&appName=amit"

# Function to connect to MongoDB
def connect_mongo():
    client = MongoClient(mongo_uri, server_api=ServerApi('1'))
    return client

# Function to process messages from Kafka
def process_message():
    consumer = Consumer(kafka_config)
    consumer.subscribe([kafka_topic])
    
    mongo_client = connect_mongo()
    db = mongo_client["cutomer_click_behaviour"]
    event_collection = db["click_data"]
    
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                continue
            try:
                value = json.loads(msg.value().decode('utf-8'))
                value["kafka_metadata"] = {
                    'topic': msg.topic(),
                    "partition": msg.partition(),
                    "offset": msg.offset(),
                    "timestamp": datetime.now().isoformat()
                }
                
                # Insert the event into MongoDB
                result = event_collection.insert_one(value)
                print(result)
            except Exception as e:
                print(e)
                
    except Exception as e:
        print(e)
            
# Main entry point
if __name__ == "__main__":
    process_message()