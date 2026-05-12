import rag_ytvideo as lch1
import streamlit as st
import textwrap

st.title("YT Assistant")

with st.sidebar:
    with st.form(key="my_form"):
        youtube_url = st.text_input(
            label="YouTube video URL"
        )

        query = st.text_area(
            label="Ask me about the video"
        )

        submit_button = st.form_submit_button(label="Submit")

if submit_button:
    if not youtube_url or not query:
        st.warning("Please enter both URL and question.")
    else:
        with st.spinner("Processing video..."):
            db = lch1.create_vector_db_fromYT(youtube_url)

        with st.spinner("Thinking..."):
            response = lch1.get_response_from_query(db, query)

        st.subheader("Answer:")
        st.write(textwrap.fill(response, width=80))