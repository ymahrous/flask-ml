install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

test:
	python3 -m pytest -vv --cov=mlib --cov=app test_mlib.py

format:
	black *.py

lint:
	pylint --disable=R,C,W1203,E1101 mlib

deploy:
	docker login
	docker build -t mlflask .
	docker tag mlflask:latest ghcr.io/ymahrous/flask-ml:latest
	docker push ghcr.io/ymahrous/flask-ml:latest
	
all: install lint test format deploy