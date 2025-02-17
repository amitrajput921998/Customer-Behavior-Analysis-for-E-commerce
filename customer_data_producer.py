import json
import streamlit as st
import time
from confluent_kafka import Producer

# Kafka configuration settings
kafka_config = { 
    'bootstrap.servers': 'pkc-619z3.us-east1.gcp.confluent.cloud:9092', 
    'security.protocol': 'SASL_SSL', 
    'sasl.mechanisms': 'PLAIN', 
    'sasl.username': 'UMZEHTYDMU423WAQN5', 
    'sasl.password': 'rJzlHQFmTzMqklVMB2wsqwedvTsUFQ0dy7h3zV9Yr/VKj//NRhJMOT21I3zTFGY5lH', 
    'group.id': 'sentiment_analysis_group', 
    'auto.offset.reset': 'earliest'
}

# Kafka topic name
kafka_topic = "customer_click_data"

# Create a Kafka producer instance
producer = Producer(kafka_config)

# Streamlit app title
st.title("Euron Big Data Customer click Analytics")

# User input fields
user_id = st.number_input("user id", min_value=1, max_value=100000, step=1)
activity = st.selectbox("activity", ["view_product", "add_to_cart", "checkout", "search", "whishlist"])
product = st.selectbox("product", ["Laptop", "mobile", "headphone", "smarthwatch", "camera", "tablet"])

# Function to send event data to Kafka
def send_event():
    event = {
        "user_id": user_id,
        "activity": activity,
        "product": product,
        "timestamp": int(time.time())
    }
    
    # Produce the event to the Kafka topic
    producer.produce(kafka_topic, key=str(user_id), value=json.dumps(event))
    producer.flush()
    
    # Display success message
    st.success(f"send this event : {event}")

# Button to trigger the send_event function
if st.button("send data"):
    send_event()