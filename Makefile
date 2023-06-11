init:
	docker-compose up --build

migrate:
	docker-compose exec web python manage.py migrate

nuke:
	docker-compose down
	docker volume rm wwc_fs_web_dev
	docker rmi wwc_fs_web_dev