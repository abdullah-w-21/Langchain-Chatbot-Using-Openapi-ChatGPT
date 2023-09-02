import PyPDF2
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import openai
import faiss
from langchain import OpenAI
import sys
import os


def query(usrtxt):
# OpenAI API key
    os.environ["OPENAI_API_KEY"] = "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"


# Get the PDF File
    reader = PdfReader('C:\\Users\\BN GAMING\\PycharmProjects\\Chatbot2\\pdf\\Veridian-01-508_Frequently Asked Questions-merged.pdf')

# Read data from the Pdf file
    pdf_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pdf_text += text

# Splitting the text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )

    texts = text_splitter.split_text(pdf_text)

# OpenAI Embeddings
    embeddings = OpenAIEmbeddings()

# Make searcher for QA
    docsearch = FAISS.from_texts(texts, embeddings)

# Make Chain object
    chain = load_qa_chain(OpenAI(), chain_type="stuff")

    #Query = input("Enter your Question: ")
    docs = docsearch.similarity_search(usrtxt)
    output = chain.run(input_documents=docs, question=usrtxt)

    return output

