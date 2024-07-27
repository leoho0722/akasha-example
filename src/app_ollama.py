from akasha import Doc_QA
from dotenv import load_dotenv
from utils import config

load_dotenv(override=True)


if __name__ == "__main__":
    app_config = config.parse_config()

    def ollama_model(prompt: str):
        from langchain_community.chat_models.ollama import ChatOllama
        model = ChatOllama(
            model=app_config.llm_config.ollama,
            temperature=0,
            verbose=True
        )
        ret = model.predict(prompt)
        return ret

    qa = Doc_QA(
        embeddings=app_config.embeddings_config.huggingface,
        model=ollama_model,
        verbose=True,
        topK=5,
        language="ch",
        search_type=app_config.akasha_config.docs_search_type,
        max_doc_len=100000000000
    )

    system_prompt = "請使用繁體中文回答"
    prompt = "如何減少鋁蓋側邊因正反面噴砂各一次的壓力過大而造成的凹坑？"
    qa.get_response(
        doc_path=app_config.akasha_config.docs_path,
        system_prompt=system_prompt,
        prompt=prompt
    )
