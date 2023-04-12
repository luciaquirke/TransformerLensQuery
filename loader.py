import pickle
import os
from llama_index import download_loader, GPTSimpleVectorIndex
from llama_index.readers import GithubRepositoryReader
from llama_index.readers.github_readers.github_api_client import GithubClient

REPO = "TransformerLens"
OWNER = "neelnanda-io"

download_loader("GithubRepositoryReader")
index = None
docs = None

if os.path.exists("../langchain.json"):
    index = GPTSimpleVectorIndex.load_from_disk("langchain.json")

if os.path.exists("TransformerLens.json"):
    index = GPTSimpleVectorIndex.load_from_disk(f"{REPO}.json")

else:
    if os.path.exists("docs.pkl"):
        with open("docs.pkl", "rb") as f:
            docs = pickle.load(f)

    if docs is None:
        github_client = GithubClient(os.getenv("GITHUB_TOKEN"))
        loader = GithubRepositoryReader(
            owner=OWNER,
            repo=REPO,
            verbose=True,
            concurrent_requests=10
        )

        docs = loader.load_data(branch="main")

        with open("docs.pkl", "wb") as f:
            pickle.dump(docs, f)

    index = GPTSimpleVectorIndex.from_documents(docs)
    index.save_to_disk(f"{REPO}.json")

print(index.query("Explain to me step by step how hooks are used in TransformerLens?"))
