.phony: test

test:
	@echo "Running tests..."
	@pytest .

dev_mode:
	@echo "Running dev mode..."
	@poetry shell && poetry install && nvim

