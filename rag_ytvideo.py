from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()


def create_vector_db_fromYT(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=False)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db


def get_response_from_query(db, query, k=4):
    docs = db.similarity_search(query, k=k)

    docs_page_content = "\n".join([d.page_content for d in docs])

    llm = OpenAI(temperature=0) 

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
You are a helpful YouTube assistant.

Answer the question using ONLY the transcript below.

Transcript:
{docs}

Question:
{question}

Answer:
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.invoke({
        "question": query,
        "docs": docs_page_content
    })

    return response["text"].replace("\n", " ")