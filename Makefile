.PHONY: run-ollama
run-ollama:
	clear && python src/app_ollama.py

.PHONY: run-openai
run-openai:
	clear && python src/app_openai.py

.PHONY: install-requirements
install-requirements:
	pip install -r src/requirements.txt