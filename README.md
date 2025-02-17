# Customer Behavior Analysis for E-commerce

## Project Overview
This project aims to analyze customer behavior on an e-commerce platform by tracking user activities such as viewing products, adding items to the cart, checking out, and more. Using a real-time data pipeline, we capture interactions through a Streamlit user interface, stream the data via Kafka, process it, and store the results in MongoDB. Finally, we connect MongoDB to Power BI for creating insightful dashboards and reports.

## Project Flow

### 1. **UI (Streamlit)**  
The project starts with a simple and interactive Streamlit interface where users input their activities such as:
- Viewing products
- Adding products to the cart
- Proceeding to checkout
- Searching for items
- Adding to wishlist

Each user interaction is captured along with the product they interacted with.

### 2. **Kafka Producer**  
Data from the Streamlit UI is sent to a Kafka topic (`customer_click_data`) using Kafka’s producer mechanism. The producer is responsible for efficiently streaming user activity data in real time to Kafka.

### 3. **Kafka Consumer**  
A Kafka consumer listens to the `customer_click_data` topic, processes the incoming data, and prepares it for storage.

### 4. **MongoDB**  
Processed data is stored in MongoDB, allowing for efficient storage of event data, which is crucial for further analysis. MongoDB’s flexibility allows us to handle large-scale event data while maintaining high performance.

### 5. **Power BI**  
MongoDB is connected to Power BI, which visualizes the data and provides business insights. Dashboards and reports are generated to help stakeholders understand user behavior and optimize the e-commerce platform for improved engagement and sales.

## Technologies Used
- **Streamlit**: Used for building an interactive user interface to collect customer behavior data in real-time.
- **Kafka (Confluent Cloud)**: A distributed event streaming platform for real-time data ingestion and processing.
- **MongoDB**: A NoSQL database used for storing user interaction data and supporting complex queries and analytics.
- **Power BI**: A business analytics tool to create dynamic dashboards and reports from the data stored in MongoDB.

## Key Features
- **Real-Time Data Processing**: All user activity is tracked and processed in real-time.
- **Scalable Data Pipeline**: Kafka allows seamless scaling of data streams to handle high traffic.
- **Interactive Dashboards**: Power BI transforms raw data into actionable business insights with rich visualizations.
- **User-Centric Analytics**: By tracking user behavior at various stages (viewing, adding to cart, checking out), businesses can improve engagement strategies and optimize sales funnels.

