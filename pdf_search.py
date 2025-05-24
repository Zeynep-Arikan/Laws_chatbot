from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain.chains import ConversationalRetrievalChain

def pdf_chat(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    llm = HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        model_kwargs={"temperature": 0.5, "max_new_tokens": 512}
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=vectorstore.as_retriever()
    )
    print("PDF Arama Modu: Kadın haklarıyla ilgili sorularınızı sorabilirsiniz.")
    chat_history = []
    while True:
        question = input("Soru: ")
        if question.lower() in ["çık", "exit", "quit"]:
            break
        result = chain({"question": question, "chat_history": chat_history})
        print("Yanıt:", result["answer"])
        chat_history.append((question, result["answer"]))