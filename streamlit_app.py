import streamlit as st
from transformers import pipeline, AutoTokenizer


# Load your fine-tuned model
@st.cache_resource #cache the model so it loads only once
def load_model():
    return pipeline("summarization", model="a2_bonus_sum_model_apurvara_asharan2")


summarizer = load_model()

st.title("Text Summarization App")

input_text = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    if input_text:
        with st.spinner("Summarizing..."):
            summary = summarizer(input_text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text.")