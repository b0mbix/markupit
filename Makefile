setup:
	poetry lock
	poetry install

test:
	poetry run pytest

tox:
	poetry run tox

clean:
	rm -rf .tox
	rm -rf */.pytest_cache
	rm -rf */__pycache__
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf .ruff_cache

pre-commit:
	poetry run pre-commit run --all-files
