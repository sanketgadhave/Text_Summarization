from src.basic_summarize import summarize_text
import streamlit as st

# Streamlit UI
st.title('Text Summarizer')

# Create a text area for input text
input_text = st.text_area("Enter Text Here to Summzarize:", height=300)


# Button to trigger summarization
if st.button('Summarize'):
    # Check if there is text to summarize
    if input_text:
        # Use the summarize_text function
        summary = summarize_text(input_text, 2)  # Adjust num_sentences as needed
        # Display the summary
        st.text_area("Summary:", value=summary, height=150, max_chars=None, help=None)
    else:
        st.write("Please enter some text to summarize.")
