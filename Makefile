# Makefile for automating common tasks in a computational research project

# The environment name (you can change this as per your virtual environment)
ENV_NAME=env

# Python interpreter
PYTHON=python3

# Install dependencies
install:
	$(PYTHON) -m venv $(ENV_NAME)
	. $(ENV_NAME)/bin/activate; pip install -r requirements.txt

# Install requirements separately if venv already exists
install-requirements:
	. $(ENV_NAME)/bin/activate; pip install -r requirements.txt

# Run the regression analysis script
run-regression:
	. $(ENV_NAME)/bin/activate; python src/analysis.py

# Clean up environment (remove virtual environment)
clean:
	rm -rf $(ENV_NAME)

# Help (display all available tasks)
help:
	@echo "Available commands:"
	@echo "  install: Install dependencies and set up virtual environment"
	@echo "  install-requirements: Install Python dependencies"
	@echo "  run-regression: Run the regression analysis script"
	@echo "  clean: Remove the virtual environment"
	@echo "  help: Display this help message"

