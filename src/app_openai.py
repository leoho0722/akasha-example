from akasha import Doc_QA
from dotenv import load_dotenv
import utils.config as config

load_dotenv(override=True)


if __name__ == "__main__":
    config = config.parse_config()

    qa = Doc_QA(
        embeddings=config.embeddings_config.openai,
        model=config.llm_config.openai,
        verbose=True,
        topK=5,
        language="ch",
        search_type=config.akasha_config.docs_search_type
    )

    system_prompt = "請使用繁體中文回答"
    prompt = "如何讓噴漆可以通同時噴在塑膠&Rubber上?"
    qa.get_response(
        doc_path=config.akasha_config.docs_path,
        system_prompt=system_prompt,
        prompt=prompt
    )
