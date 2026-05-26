from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

from langchain_core.documents import (
    Document
)

import os


DB_DIR = "vector_db"


embedding_model = HuggingFaceEmbeddings(

    model_name=
    "sentence-transformers/all-MiniLM-L6-v2"
)


vectorstore = Chroma(

    persist_directory=DB_DIR,

    embedding_function=embedding_model
)


def store_incident_logs(logs):

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

        vectorstore.add_documents(
            documents
        )

        vectorstore.persist()


def search_similar_incidents(query):

    results = vectorstore.similarity_search(

        query,

        k=3
    )

    return [

        result.page_content

        for result in results
    ]