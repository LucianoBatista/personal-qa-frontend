import requests


def create_question(question: str, answer: str, tags: list[str]):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    json_data = {
        "user_id": 1,
        "question_text": question,
        "question_tags": tags,
        "answer_text": answer,
    }

    response = requests.post(
        "http://web:8000/questions/create_question",
        headers=headers,
        json=json_data,
    )
    return response


def get_question(question_id: int):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    params = {
        "id": str(question_id),
    }

    response = requests.get(
        "http://web:8000/questions/get_question",
        headers=headers,
        params=params,
    )
    return response


def update_question_crud(
    question_id: int, question: str, answer: str, tags: list[str] = []
):
    """
    For now we'll not update the tags field
    """
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    json_data = {
        "question_id": question_id,
        "question_text": question,
        "answer_text": answer,
    }

    response = requests.put(
        "http://web:8000/questions/put_question",
        headers=headers,
        json=json_data,
    )
    return response


def get_questions_by_tags(tags: list[str], n_questions: int):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    body = {
        "tag": tags,
        "n_question": n_questions,
    }

    response = requests.post(
        "http://web:8000/questions/by_tag",
        headers=headers,
        json=body,
    )
    return response
