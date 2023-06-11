init:
	docker-compose up --build -d

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

shell:
	docker-compose exec web python manage.py shell

seed-data:
	docker-compose exec web python manage.py runscript make_seed_data
