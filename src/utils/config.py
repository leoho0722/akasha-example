import yaml


class EmbeddingsModelConfig:
    """
    定義 Embeddings Model Config

    Parameters:
        openai (str): OpenAI 提供的 Embeddings Model 名稱，例如：`text-embedding-3-small`
        huggingface (str): HuggingFace 提供的 Embeddings Model 名稱，例如：`all-MiniLM-L6-v2`
    """

    def __init__(
        self,
        openai: str,
        huggingface: str
    ) -> None:
        self.openai = f"openai:{openai}"
        self.huggingface = f"huggingface:{huggingface}"


class LLMConfig:
    """
    定義 LLM (Large Language Model) Config

    Parameters:
        openai (str): OpenAI 提供的 LLM 名稱，例如：`gpt-4o-mini`
        ollama (str): Ollama 提供的 LLM 名稱，例如：`gemma2:9b`
        huggingface (str): HuggingFace 提供的 LLM 名稱，例如：`meta-llama/Llama-2-13b-chat-hf`
        llamaCpp (str): 使用 llama.cpp 進行量化後的 LLM 名稱，例如：`llama-2-13b-chat.Q5_K_S.gguf`
        use_gpu (bool): 是否使用 GPU，預設為 `False`
    """

    def __init__(
        self,
        openai: str,
        ollama: str,
        huggingface: str,
        llamaCpp: str,
        use_gpu: bool = False
    ) -> None:
        self.openai = f"openai:{openai}"
        self.ollama = ollama
        self.huggingface = f"hf:{huggingface}"
        if use_gpu:
            self.llamaCpp = f"llama-gpu:model/{llamaCpp}"
        else:
            self.llamaCpp = f"llama-cpu:model/{llamaCpp}"


class AkashaConfig:
    """
    定義 Akasha Config

    Parameters:
        docs_path (str): 用來進行文檔檢索的資料夾路徑
        docs_search_type (str): 要進行文檔檢索的搜尋方式，分為 `svm`、`mmr`、`tfidf`、`KNN`、`bm25`，預設為 `svm`
    """

    def __init__(
        self,
        docs_path: str,
        docs_search_type: str = "svm"
    ) -> None:
        self.docs_path = docs_path
        self.docs_search_type = docs_search_type


class Config:
    """
    定義 config.yaml 中的參數

    Parameters:
        llm_config (LLMConfig): 定義 LLM Config
        embeddings_config (EmbeddingsModelConfig): 定義 Embeddings Model Config
        akasha_config (AkashaConfig): 定義 Akasha Config
    """

    def __init__(
        self,
        llm_config: LLMConfig,
        embeddings_config: EmbeddingsModelConfig,
        akasha_config: AkashaConfig
    ) -> None:
        self.llm_config = llm_config
        self.embeddings_config = embeddings_config
        self.akasha_config = akasha_config


def parse_config(file_path: str = "src/config.yaml") -> Config:
    """
    解析 config.yaml 中的參數

    Parameters:
        file_path (str): config.yaml 的檔案路徑

    Raises:
        ValueError

    Returns:
        config (Config): 解析出來的 Config 參數
    """

    if file_path == "":
        raise ValueError("file_path is required")

    with open(file_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return _new_config(config)


def _new_config(config) -> Config:
    """
    將解析出來的 config 參數，轉換成 `Config` object

    Parameters:
        config (object): 從 config.yaml 中解析出來的內容

    Returns:
        config (Config): 解析出來的 Config 參數
    """

    model = config["model"]
    llm = model["llm"]
    openai_llm = llm["openai"]
    ollama_llm = llm["ollama"]
    huggingface_llm = llm["huggingface"]
    llamaCpp_llm = llm["llamaCpp"]
    llamaCpp_llm_name = llamaCpp_llm["name"]
    llamaCpp_use_gpu = llamaCpp_llm["useGPU"]
    
    embeddings = model["embeddings"]
    openai_embeddings = embeddings["openai"]
    huggingface_embeddings = embeddings["huggingface"]

    akasha = config["akasha"]
    docs = akasha["docs"]
    docs_path = docs["path"]
    docs_search_type = docs["searchType"]

    return Config(
        llm_config=LLMConfig(
            openai=openai_llm,
            ollama=ollama_llm,
            huggingface=huggingface_llm,
            llamaCpp=llamaCpp_llm_name,
            use_gpu=llamaCpp_use_gpu
        ),
        embeddings_config=EmbeddingsModelConfig(
            openai=openai_embeddings,
            huggingface=huggingface_embeddings
        ),
        akasha_config=AkashaConfig(
            docs_path=docs_path,
            docs_search_type=docs_search_type
        )
    )
