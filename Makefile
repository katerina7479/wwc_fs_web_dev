init:
	docker-compose up --build

migrate:
	docker-compose exec web python manage.py migrate

schema_migration:
	docker-compose exec web python manage.py makemigrations

list:
	docker-compose ps

nuke:
	docker-compose down
	docker volume rm wwc_fs_web_dev_pgdata
	docker rmi wwc_fs_web_dev-web

create-superuser:
	docker-compose exec web python manage.py createsuperuser
