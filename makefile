# Use Poetry for dependency management and running tasks

# Target to install dependencies
install:
	poetry install

# Target to update dependencies
update:
	poetry update

# Target to export requirements.txt for compatibility
requirements:
	poetry export -f requirements.txt --output requirements/base.txt --without-hashes

# Target to run linting
lint:
	poetry run flake8 .

# Target to run the application
	poetry run python src/main.py

# Clean up cache files, etc.
clean:
	rm -rf .pytest_cache .mypy_cache
	find . -name "*.pyc" -delete

# Target to build the package
build:
	poetry build

# Help target to display available commands
help:
	@echo "Available commands:"
	@echo "  install       Install project dependencies"
	@echo "  update        Update project dependencies"
	@echo "  requirements  Export dependencies to requirements.txt"
	@echo "  lint          Run linting"
	@echo "  run           Run the application"
	@echo "  clean         Remove cache files"
	@echo "  build         Build the package"