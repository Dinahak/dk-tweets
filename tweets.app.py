# streamlit_app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Set the title
st.title("Twitter Airline Sentiment Analysis")

# Load dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/Dinahak/dk-tweets/refs/heads/main/Tweets.csv"
    return pd.read_csv(url)

tweets = load_data()

# Show data
st.subheader("Sample of Tweet Data")
st.dataframe(tweets.head())

# Pie chart: Sentiment Count
st.subheader("Sentiment Distribution")

sentiment_count = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_count.columns = ['airline_sentiment', 'count']

fig_pie = px.pie(
    sentiment_count,
    values='count',
    names='airline_sentiment',
    title='Sentiment Count of Tweets'
)
st.plotly_chart(fig_pie)

# Bar chart: Tweet Count by Airlines
st.subheader("Tweet Count by Airlines")

airline_count = tweets['airline'].value_counts().reset_index()
airline_count.columns = ['airline', 'count']

plt.figure(figsize=(10, 6))
sns.barplot(x='airline', y='count', hue='airline', palette='pastel', legend=False, data=airline_count)
plt.title('Tweet Count by Airlines')
plt.xlabel('Airline')
plt.ylabel('Tweet Count')

# Show matplotlib plot in Streamlit
st.pyplot(plt)
