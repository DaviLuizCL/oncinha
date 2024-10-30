req:
	@pip freeze > requirements.txt

build:
	@docker build -t appinicial .

compose:
	@docker-compose build
	@docker-compose up