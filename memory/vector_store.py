from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

from langchain_core.documents import (
    Document
)


DB_DIR = "vector_db"

vectorstore = None


def get_vectorstore():

    global vectorstore

    if vectorstore is None:

        embedding_model = HuggingFaceEmbeddings(

            model_name=
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        vectorstore = Chroma(

            persist_directory=DB_DIR,

            embedding_function=embedding_model
        )

    return vectorstore


def store_incident_logs(logs):

    vector_db = get_vectorstore()

    documents = []

    for log in logs:

        content = f"""

        Service:
        {log.get('service')}

        Severity:
        {log.get('severity')}

        Message:
        {log.get('message')}
        """

        documents.append(

            Document(

                page_content=content,

                metadata={

                    "service":
                        log.get("service"),

                    "severity":
                        log.get("severity")
                }
            )
        )

    if documents:

        vector_db.add_documents(
            documents
        )


def search_similar_incidents(query):

    vector_db = get_vectorstore()

    results = vector_db.similarity_search(

        query,

        k=3
    )

    return [

        result.page_content

        for result in results
    ]