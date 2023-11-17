import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.sidebar.success("Select what you want to do")

st.markdown(
    """
            # :technologist: Your Personal Learning Environment

Welcome to your personal question and answering application, where it primary objective is to serve as a personalized question answering platform. This platform empowers you to enhance your knowledge and skills in any subject of your choice.

I'm continuously enhancing this project to provide you with a comprehensive set of features, for now the application is supporting:

- :white_check_mark: **Question Creation**: Craft and submit your own questions to the platform.
- :white_check_mark: **Answer Management**: Append answers to questions, creating a valuable knowledge base.
- :white_check_mark: **Local Datastore**: Designed with a focus on personal use, I'm providing a local datastore (sqlite). You can easily switch to a MySQL database by modifying the configuration. Thanks to SQLAlchemy, the process is simple.
- :white_check_mark: **Tag Registration**: Categorize questions for easy retrieval, even without AI assistance. Every tag passed during the question registration is saved on the database.

To be implemented...:
- [ ] **AI-Powered Answer Generation**: Leverage AI technology to automatically generate answers for your questions.
- [ ] **Space Repetition Algorithm**: Employ a spaced repetition algorithm to optimize your learning and memory retention.
- [ ] **Vector Database Connection**: Streamline question retrieval with a vector database connection, making it easier to locate your questions.
- [ ] **User Registration**: Sign up for a personalized experience and track your progress.
- [ ] **AI-Based Question Creation**: Generate questions based on existing text context, making learning more intuitive.
- [ ] **AI-Powered Answer Correction**: Utilize AI to improve the accuracy of your answers.
- [ ] **AI-Duplication Detector**: Utilize AI to detect which question is duplicated. Besides we could search for exact same text, is better to search for very similar questions.
            """
)
