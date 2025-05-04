# Makefile for automating common tasks in a computational research project

# The environment name (you can change this as per your virtual environment)
ENV_NAME=env

# Python interpreter
PYTHON=python3

# Install dependencies
install:
	$(PYTHON) -m venv $(ENV_NAME)  # Create virtual environment
	. $(ENV_NAME)/bin/activate; pip install -r requirements.txt  # Install from requirements.txt

# Install requirements
install-requirements:
	. $(ENV_NAME)/bin/activate; pip install -r requirements.txt

# Run data exploration notebook
explore:
	. $(ENV_NAME)/bin/activate; jupyter notebook data-exploration.ipynb

# Run the regression analysis script
run-regression:
	. $(ENV_NAME)/bin/activate; python analysis.py

# Clean up environment (remove virtual environment)
clean:
	rm -rf $(ENV_NAME)

# Help (display all available tasks)
help:
	@echo "Available commands:"
	@echo "  install: Install dependencies"
	@echo "  install-requirements: Install requirements from requirements.txt"
	@echo "  explore: Run data exploration notebook"
	@echo "  run-regression: Run the regression analysis script"
	@echo "  clean: Clean up virtual environment"
	@echo "  help: Display this message"

