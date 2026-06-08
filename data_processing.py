from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def document_loader(file):
    loader=PyPDFLoader(file.name)
    loaded_document= loader.load()
    return loaded_document

def text_splitter(data):
    text_splitter= RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks= text_splitter.split_documents(data)
    return chunks