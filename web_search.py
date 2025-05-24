from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain.chains import ConversationalRetrievalChain


def web_chat():
    urls = [
        "https://www.unwomen.org/en/news/in-focus/csw/women-and-the-law",
        "https://kadininstatusu.aile.gov.tr/mevzuat",
        # İstediğin kadın haklarıyla ilgili başka kaynakları da ekleyebilirsin.
    ]
    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    doc_splits = text_splitter.split_documents(docs_list)

    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="kadin-haklari-chroma",
        embedding=OpenAIEmbeddings(),
    )
    retriever = vectorstore.as_retriever()

    llm = HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        model_kwargs={"temperature": 0.5, "max_new_tokens": 512}
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

    print("Web Arama Modu: Kadın haklarıyla ilgili sorularınızı sorabilirsiniz.")
    chat_history = []
    while True:
        question = input("Soru: ")
        if question.lower() in ["çık", "exit", "quit"]:
            break
        result = chain({"question": question, "chat_history": chat_history})
        print("Yanıt:", result["answer"])
        chat_history.append((question, result["answer"]))
