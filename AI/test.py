from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv


load_dotenv()

# 임베딩
embeddings = OpenAIEmbeddings()

db = FAISS.load_local(
    folder_path="faiss_db",
    index_name="faiss_index",
    embeddings=embeddings,
    allow_dangerous_deserialization=True,
)
res = db.similarity_search("What is Love", filter={'source': "User1_dating advice ai"})
# print(db.docstore._dict)
print(res)