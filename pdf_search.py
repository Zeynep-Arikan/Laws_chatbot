import os
from glob import glob
from langchain_community.llms import HuggingFaceHub
from langchain.chains import ConversationalRetrievalChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader



def pdf_chat_from_folder(folder_path):
    # Tüm PDF dosyalarının yollarını al
    pdf_files = glob(os.path.join(folder_path, "*.pdf"))
    
    # PDF'leri yükle
    documents = []
    for pdf_file in pdf_files:
        loader = PyPDFLoader(pdf_file)
        documents.extend(loader.load())

    # Metni böl
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(documents)

    # Vektör veritabanı oluştur
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    # LLM yükle
    llm = HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        model_kwargs={"temperature": 0.5, "max_new_tokens": 512}
    )

    # Konuşma zinciri kur
    chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=vectorstore.as_retriever()
    )

    # Soru-cevap döngüsü
    print("PDF Arama Modu: Kadın haklarıyla ilgili tüm PDF'lerde arama yapabilirsiniz.")
    chat_history = []
    while True:
        question = input("Soru: ")
        if question.lower() in ["çık", "exit", "quit"]:
            break
        result = chain({"question": question, "chat_history": chat_history})
        print("Yanıt:", result["answer"])
        chat_history.append((question, result["answer"]))
