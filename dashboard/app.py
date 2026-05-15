import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# -----------------------------
# DATABASE CONFIG
# -----------------------------

DB_HOST = "news-pipeline-db.c1iccwg44xf2.ap-south-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "NewsPipeline123"
DB_PORT = "5432"

# -----------------------------
# CONNECT TO DATABASE
# -----------------------------

engine = create_engine(
    f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# -----------------------------
# LOAD DATA
# -----------------------------

query = """
SELECT *
FROM news_articles
ORDER BY published_at DESC
LIMIT 100
"""

df = pd.read_sql(query, engine)

# -----------------------------
# STREAMLIT UI
# -----------------------------

st.set_page_config(
    page_title="News Pipeline Dashboard",
    layout="wide"
)

st.title("📰 News Pipeline Dashboard")

st.subheader("Latest News Articles")

st.dataframe(df)

# -----------------------------
# SENTIMENT COUNTS
# -----------------------------

if "sentiment" in df.columns:

    st.subheader("Sentiment Distribution")

    sentiment_counts = df["sentiment"].value_counts()

    st.bar_chart(sentiment_counts)