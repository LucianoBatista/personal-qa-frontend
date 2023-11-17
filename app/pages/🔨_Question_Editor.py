import streamlit as st
from streamlit_quill import st_quill
from services.backend.question_crud import get_question
from callbacks.callbacks import update_question

st.title("Question Editor")

st.markdown("## Check the question you want to edit.")
question_id = st.number_input(
    "Question ID",
    min_value=1,
    key="question_id",
)

if question_id:
    # TODO: implement the question text retrieve from the batabase, through the API
    response = get_question(int(question_id))

    if response.status_code != 200:
        st.error("Question not found")
    else:
        question_text = response.json()["question"]
        answer_text = response.json()["answer"]
        # question_text = "Q: How many layers exist on the transformer models? \n```python\nf= open('demofile.txt', 'r')\nprint(f.read())\n```\n"
        st.markdown("Q: " + question_text)
        # answer_text = "R: There are 6 layers on the transformer models"
        st.markdown("R: " + answer_text)

# ------------------------------
st.markdown("---")
st.markdown("## Put your question here and edit.")
st.markdown("### Question")
question = st_quill(key="question_editor", placeholder="Enter the question")
st.write(question)
st.markdown("### Answer")
answer = st_quill(key="answer_editor", placeholder="Enter the solution")
st.write(answer)
button = st.button("Edit", on_click=update_question)
