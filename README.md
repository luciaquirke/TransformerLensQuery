# TransformerLensQuery
Query the TransformerLens repo using llama_index and langchain. Requires an OpenAI API key.

### Setup Option 1

Grab `query.py` and `TransformerLens.json`, download the packages used in `query.py` 

### Setup Option 2

Install Python 3.11 and Poetry, then run

```
poetry install                                                       
```

### Usage

```
OPENAI_API_KEY=$OPENAI_API_KEY poetry run python query.py query "What's a use case for TransformerLens' activation hooks?"
❯ A use case for TransformerLens' activation hooks is to enable exploratory analysis of language models. By caching any internal 
activation in the model, and adding in functions to edit, remove or replace these activations as the model runs, users can quickly
and easily explore the inner workings of the model and gain insights into how it works. This can be used to reverse engineer algorithms 
the model learned during training from its weights, and to gain a better understanding of how language models work.
```
