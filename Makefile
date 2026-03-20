install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
# 	python -m pytest  --nbval-lax *.ipynb
# 	python -m pytest -vv --cov=hello --cov=cli test_*.py
	python -m pytest -vv --cov=hello --cov=main --cov=calCLI --cov=mylib test_*.py

format:
	black *.py mylib/*.py

lint:
	python -m pylint *.py mylib/*.py
	
refactor: format lint

deploy:
#echo "deploy not implemented"

all: install lint test format deploy
