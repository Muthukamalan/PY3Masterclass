.PHONY: clean lint
.DEFAULT_GOAL := help


SHELL := /bin/bash
.ONESHELL:
.SILENT:

# =============================
# Project Config
# =============================
SRC := app
HOST := 0.0.0.0
PORT := 8000


help: ## Show available targets
	@awk 'BEGIN {FS = ":.*## "; printf "\nAvailable targets:\n"} /^[a-zA-Z0-9_-]+:.*## / { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

clean: ## Remove caches and generated artifacts
	@find . -type d \( -name "__pycache__" -o -name "outputs" -o -name ".ruff_cache" -o -name "multirun"  -o -name "logs" -o -name "logs" -o -name "mlruns" \) -exec rm -rf {} +


start: ## Start the application
	@uvicorn app.main:app --host $(HOST) --port $(PORT) --reload

	
# -----------------------------
# Quality gates (production pattern)
# -----------------------------
lint: ## Format code with black and ruff
	@ruff check $(SRC) --fix