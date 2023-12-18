# import
import os
import argparse
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

def loadChroma(filename: str) -> Chroma:
    # load the document and split it into chunks
    loader = TextLoader(filename)
    documents = loader.load()

    # split it into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # load it into Chroma
    db = Chroma.from_documents(docs, embedding_function, persist_directory="./chroma_db")
    return db

def queryChroma(db: Chroma, query: str) -> list:
    # query it
    docs = db.similarity_search(query)
    return docs

def main():
    parser = argparse.ArgumentParser(description='Embed document, query chromadb')
    parser.add_argument('-f', '--file', type=str, help='The file to embed')
    parser.add_argument('-q', '--query', type=str, help='query', default=None)
    args = parser.parse_args()

    # check if file exists
    if not os.path.exists(args.file):
        print('File does not exist')
        return

    db = loadChroma(args.file)
    if(args.query):
        docs = queryChroma(db, args.query)
        print(docs[0].page_content)

if __name__ == '__main__':
    main()

