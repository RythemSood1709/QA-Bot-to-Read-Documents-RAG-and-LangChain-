from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

from models import get_llm, watsonx_embedding
from data_processing import document_loader, text_splitter

def vector_database(chunks):
    embedding_model=watsonx_embedding()
    vectordb= Chroma.from_documents(documents=chunks,embedding=embedding_model)
    return vectordb

def retriever(file):
    splits= document_loader(file)
    chunks=text_splitter(splits)
    vectordb=vector_database(chunks)
    retriever= vectordb.as_retriever()
    return retriever


def retriever_qa(file, query):
    llm= get_llm()
    retriever_obj= retriever(file)
    qa=RetrievalQA.from_chain_type(llm=llm, chain_type="map_reduce", retriever=retriever_obj, return_source_documents=True)

    response= qa.invoke(query)
    return response['result']