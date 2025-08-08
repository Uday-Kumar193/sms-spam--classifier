import os
os.environ["STREAMLIT_DISABLE_LOGGING"] = "1"
os.environ["STREAMLIT_TELEMETRY"] = "0"

import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required resources
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')

# Initialize stemmer
ps = PorterStemmer()




# Preprocessing
def transform_text(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.isalnum()]
    words = [word for word in words if word not in stopwords.words('english')]
    words = [ps.stem(word) for word in words]
    return " ".join(words)


# Load model/vectorizer
@st.cache_resource
def load_model():
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
    classifier = pickle.load(open('model.pkl', 'rb'))
    return vectorizer, classifier


tfidf, model = load_model()

# Page config
st.set_page_config(page_title="SMS Spam Classifier", page_icon="📨", layout="centered")

# Sidebar Info
with st.sidebar:
    st.header("📌 About")
    st.markdown("""
    This project uses **Natural Language Processing** and **Machine Learning** to classify SMS messages as **Spam** or **Not Spam**.

    - Uses **TF-IDF** for vectorization
    - Model: Trained with a classic ML algorithm
    - Developed with ❤️ by **Uday Kumar**
    """)
    st.markdown("---")
    st.markdown("📫 Contact Me:- uday739987@gmail.com")

# CSS Styling
st.markdown("""
    <style>
    .stTextArea>div>textarea {
        background-color: #f0f4ff;
        border: 2px solid #4682B4;
        border-radius: 0.5rem;
        font-size: 16px;
    }
    .stButton button {
        background-color: #4682B4;
        color: white;
        font-weight: bold;
        border-radius: 0.5rem;
        font-size: 16px;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📨 SMS Spam Classifier")
st.markdown("### 🔍 Detect whether a message is Spam or Not in one click!")

# Input
input_sms = st.text_area("✉️ Enter the SMS message:", placeholder="Type your SMS here...")

# Prediction
if st.button("🚀 Predict"):
    if input_sms.strip():
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        result = model.predict(vector_input)[0]

        if result == 1:
            st.error("⚠️ This message is classified as **SPAM**.")
        else:
            st.success("✅ This message is classified as **Not Spam**.")
    else:
        st.warning("⚠️ Please enter a message before prediction.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center>🔧 Developed by <strong>Uday Kumar</strong> | 📅 2025</center>", unsafe_allow_html=True)
