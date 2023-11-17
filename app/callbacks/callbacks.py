import streamlit as st
from services.backend.question_crud import create_question, update_question_crud


def clean_state():
    st.session_state["answer_editor"] = None
    st.session_state["question_editor"] = None
    st.session_state["tags"] = []
    st.session_state["new_tags"] = ""
    st.session_state["tags_from_db_user"] = []


def register_question():
    question_text = st.session_state["question_editor"]
    answer_text = st.session_state["answer_editor"]
    tags_text = st.session_state["tags"]
    response = create_question(question_text, answer_text, tags_text)

    if response.status_code == 200:
        id_ = response.json()["question_id"]
        st.success("ID: {} was registered successfully!".format(id_))
    else:
        st.error("Error: {}".format(response.json()["detail"]))


def update_question():
    question_id = st.session_state["question_id"]
    question_text = st.session_state["question_editor"]
    answer_text = st.session_state["answer_editor"]
    response = update_question_crud(question_id, question_text, answer_text)

    if response.status_code == 200:
        st.success("ID: {} was edited successfully!".format(question_id))
    else:
        st.error("Error: {}".format(response.json()["detail"]))


def master_callback():
    register_question()
    clean_state()
