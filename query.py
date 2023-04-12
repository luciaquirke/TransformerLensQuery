from llama_index import GPTSimpleVectorIndex

index: GPTSimpleVectorIndex | None = None


def query_transformer_lens(query: str):
    index = GPTSimpleVectorIndex.load_from_disk(f"TransformerLens.json")
    print(index.query(query))


if __name__ == "__main__":
    import fire
    fire.Fire(
        dict(
            query=query_transformer_lens,
        )
    )
