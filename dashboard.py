
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the Streamlit app
st.title('Customer Review Analysis Based on Delivery Delays and Geographic Location')

# Introduction section
st.header('Introduction')
st.write('This project analyzes customer reviews based on delivery delays and customer satisfaction in different regions.')

# Dataset Loading
st.header('Dataset Loading')
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write('Dataset Loaded Successfully!')
    st.write(data.head())

    # Exploratory Data Analysis
    st.header('Exploratory Data Analysis (EDA)')

    # Display histograms of review scores
    st.subheader('Histogram of Review Scores')
    fig, ax = plt.subplots()
    ax.hist(data['review_score'], bins=5, edgecolor='black')
    ax.set_title('Distribution of Review Scores')
    ax.set_xlabel('Review Score')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Bar chart of delivery delays vs customer satisfaction
    st.subheader('Delivery Delays and Customer Satisfaction')
    fig, ax = plt.subplots()
    ax.scatter(data['delivery_delay'], data['review_score'])
    ax.axhline(y=3, color='r', linestyle='--')
    ax.set_title('Delivery Delays vs Customer Satisfaction')
    ax.set_xlabel('Delivery Delay (days)')
    ax.set_ylabel('Review Score (1-5)')
    st.pyplot(fig)

    # Bar chart of review scores by region/state
    st.subheader('Customer Satisfaction by Region')
    avg_review_by_state = data.groupby('state')['review_score'].mean()
    fig, ax = plt.subplots()
    avg_review_by_state.plot(kind='bar', ax=ax)
    ax.axhline(y=3, color='r', linestyle='--')
    ax.set_title('Average Review Score by State')
    ax.set_xlabel('State')
    ax.set_ylabel('Average Review Score (1-5)')
    st.pyplot(fig)

    # Conclusion section
    st.header('Conclusion')
    st.write('- **Delivery Delays Impact Customer Satisfaction**: Late deliveries tend to result in lower review scores.')
    st.write('- **Satisfaction Varies by Region**: Some regions have lower average review scores, indicating areas for improvement.')
