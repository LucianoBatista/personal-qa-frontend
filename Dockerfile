FROM python:3.11.0-slim-buster

LABEL maintainer='luba'

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
# set working directory
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# copying requirements
COPY Pipfile* ./

RUN pip install -q --no-cache-dir \
    pipenv===2023.3.20 && \
    pipenv install --system

COPY ./ ./

ENTRYPOINT ["streamlit", "run", "app/🏠_Home.py", "--server.port=8501", "--server.address=0.0.0.0"]

