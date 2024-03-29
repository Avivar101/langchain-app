import streamlit as st
import lc_helper
import textwrap

st.title("YouTube Assistant")
with st.sidebar:
    with st.form(key="my form"):
        youtube_url = st.sidebar.text_area(
            label="paste youtube url",
            max_chars=50
        )
        
        submit_button = st.form_submit_button(label="Submit")

if youtube_url:
    db = lc_helper.ceate_vector_db_from_youtube(youtube_url)
    responce = lc_helper.get_response_from_query(db)
    st.subheader("Answer")
    st.text(textwrap.fill(responce, width=80))