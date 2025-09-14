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
	docker login --username AWS --password-stdin amazonaws.com
	docker build -t mlflask .
	docker tag mlflask:latest /mlops:latest
	docker push /mlops:latest
	
all: install lint test format

#lint Dockerfile
#docker run --rm -i hadolint/hadolint < Dockerfile
#deploy