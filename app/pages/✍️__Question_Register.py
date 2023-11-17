import streamlit as st
from streamlit_quill import st_quill
from services.backend.tags_crud import get_all_tags
from callbacks.callbacks import master_callback, register_question

st.title("Question Register")

question = st_quill(key="question_editor")
st.write(question)

# ------------------------------
st.title("Answer Register")

answer = st_quill(key="answer_editor")
st.write(answer)

# ------------------------------
# tags from the database [] + tags registered by the user []
col1, col2 = st.columns(2)
with col1:
    response = get_all_tags()
    tags_from_db = response.json()
    tags_from_db_user = st.multiselect(
        "Tags",
        tags_from_db,
        key="tags_from_db_user",
    )
with col2:
    new_tags = st.text_input("New Tags", key="new_tags", help="Separate by comma")

# adapt to a list of tags
tags = tags_from_db_user + new_tags.split(",")
st.session_state["tags"] = [tag.strip() for tag in tags]

# ------------------------------
button = st.button("Register", on_click=master_callback)
