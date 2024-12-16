# Akasha Example

[Akasha Offical GitHub Repository](https://github.com/iii-org/akasha)
[Akasha Offical Chinese Manual](https://hackmd.io/@akasha-terminal-2024/ryS4pS1ca)

## Install

### Create and Activate Virtual Environment

```shell
python3.10 -m venv .venv
source .venv/bin/activate
```

### Packages

```shell
# In Virtual Environment
pip install -r src/requirements.txt

# or
make install-requirements
```

### Environment Variables

Copy `src/.envExample` to `src/.env` and edit it.

```shell
# In src/.env
OPENAI_API_KEY=<YOUR OPENAI API KEY>
HF_TOKEN=<YOUR HUGGINGFACE TOKEN>
```

### Config

```yaml
model:
  llm:
    openai: "gpt-4o-mini"
    ollama: "gemma2:9b"
    huggingface: "meta-llama/Llama-2-13b-chat-hf"
    llamaCpp:
      name: "llama-2-13b-chat.Q5_K_S.gguf"
      useGPU: true
  embeddings:
    openai: "text-embedding-3-small"
    huggingface: "all-MiniLM-L6-v2"
akasha:
  docs:
    path: "docs/Default/"
    # Search Type，有以下五種搜尋方式
    # svm、mmr、tfidf、KNN、bm25
    # 預設為 svm
    # https://hackmd.io/@akasha-terminal-2024/ryS4pS1ca/%2F9Bhsju1sRBeV3Zo5ONRgcw
    searchType: "svm"
```

## Run

### OpenAI

```shell
make run-openai
```

### Ollama

```shell
make run-ollama
```
