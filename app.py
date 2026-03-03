import streamlit as st
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# PAGE CONFIG
st.set_page_config(page_title="Vendor Recommendation System", layout="wide")

st.title("🏢 Vendor Recommendation System")
st.write("Find the most relevant vendors based on work, category and rating.")

# LOAD DATA
@st.cache_data
def load_data():
    df = pd.read_csv("vendors.csv")
    df = df.dropna()
    return df

df = load_data()

# FEATURE ENGINEERING
df["combined_text"] = df["Work_Type"] + " " + df["Category"]

vectorizer = TfidfVectorizer()
text_vectors = vectorizer.fit_transform(df["combined_text"])

scaler = MinMaxScaler()
rating_scaled = scaler.fit_transform(df[["Rating"]])

# Give 80% weight to text, 20% to rating
final_features = np.hstack((text_vectors.toarray()*0.8, rating_scaled*0.2))

similarity_matrix = cosine_similarity(final_features)

# SIDEBAR INPUT
st.sidebar.header("🔍 New Project Requirements")

input_work = st.sidebar.text_input("Work Type", "AI ML")
input_category = st.sidebar.text_input("Category", "IT")
input_rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 4.5)

# RECOMMENDATION FUNCTION
def recommend_for_new_project(work, category, rating, top_n=5):

    input_text = work + " " + category

    input_vector = vectorizer.transform([input_text])
    input_rating_scaled = scaler.transform([[rating]])

    input_final = np.hstack((input_vector.toarray()*0.8,
                             input_rating_scaled*0.2))

    similarities = cosine_similarity(input_final, final_features)

    sorted_scores = sorted(
        list(enumerate(similarities[0])),
        key=lambda x: x[1],
        reverse=True
    )

    top_indices = [i[0] for i in sorted_scores[:top_n]]

    return df.iloc[top_indices]

#SHOW RESULTS
if st.sidebar.button("Find Vendors"):

    results = recommend_for_new_project(
        input_work,
        input_category,
        input_rating
    )

    st.subheader("📌 Recommended Vendors")
    st.dataframe(results[["Company", "Work_Type", "Category", "Rating"]])

    st.success("Top vendors selected based on similarity score.")