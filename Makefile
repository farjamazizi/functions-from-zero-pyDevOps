install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
# 	python -m pytest  --nbval-lax *.ipynb
# 	python -m pytest -vv --cov=hello --cov=cli test_*.py
	python -m pytest -vv --cov=hello --cov=calCLI --cov=mylib test_*.py

format:
	black *.py mylib/*.py

lint:
	pylint --disable=R,C *.py mylib/*.py --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*py *
	
refactor: format lint

deploy:
#echo "deploy not implemented"

all: install lint test format deploy
