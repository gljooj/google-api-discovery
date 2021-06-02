-include .env
export

install:
	docker-compose build

run:
	docker-compose up -d

extract:
	docker-compose exec web bash -c 'python manage.py customers_bulkupsert --path customers.csv'

test:
	docker-compose run web python manage.py test

stop:
	docker-compose down