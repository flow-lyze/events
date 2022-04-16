setup:
	pip3 install -r requirements.txt
run:
	uvicorn app.main:server --reload

build:
	echo "Composing service-api project..."
	docker-compose up