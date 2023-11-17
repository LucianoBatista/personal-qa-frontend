import streamlit as st
from services.backend.tags_crud import get_all_tags
from services.backend.question_crud import get_questions_by_tags


def get_tags():
    tags = get_all_tags()

    if tags.status_code != 200:
        st.error("Tags not found")
        return []
    else:
        return tags.json()


@st.cache_data(persist="disk")
def get_questions(tags: list, n_questions: int):
    response = get_questions_by_tags(tags, n_questions)
    if response.status_code != 200:
        st.error("Questions not found")
        return []
    else:
        data = response.json()
        return data


def increment_counter():
    if st.session_state.count < st.session_state.n_question - 1:
        st.session_state.count += 1


def reset_increment_counter():
    st.session_state.count = 0


st.title("Let's Practice")

if "count" not in st.session_state:
    st.session_state.count = 0

if "n_question" not in st.session_state:
    st.session_state.n_question = 0

st.markdown(
    "## On this first step, you will practice every thing you have learned so far"
)


st.multiselect(
    "Choose the tags you want to practice",
    get_tags(),
    key="tags",
    on_change=reset_increment_counter,
)

st.number_input(
    "Choose how much questions you want to practice",
    key="quantity",
    min_value=1,
    on_change=reset_increment_counter,
)

st.multiselect(
    "Choose the difficulty level",
    ["Easy", "Medium", "Hard"],
    key="difficulty",
    disabled=True,
)

st.multiselect(
    "Choose the type",
    ["Multiple Choice", "True or False", "Text"],
    key="type",
    disabled=True,
)


n_questions = st.session_state["quantity"]
tags = st.session_state["tags"]
difficulty = st.session_state["difficulty"]
type_ = st.session_state["type"]
questions = get_questions(tags, n_questions)
st.session_state.questions = questions
st.session_state.n_question = n_questions

try:
    question = st.session_state.questions[st.session_state.count]["question"]
except IndexError:
    question = None
    st.error("No more questions")

st.markdown(f"### Question {st.session_state.count + 1}")
st.markdown(question)
ans_button = st.button("Show Answer")
if ans_button:
    answer = st.session_state.questions[st.session_state.count]["answer"]
    st.markdown(f"**{answer}**")


ans_button = st.button("Next", on_click=increment_counter)
