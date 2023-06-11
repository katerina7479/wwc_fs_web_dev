## Setting up the skeleton

### Recommended, potentially optional
1. Install virtualenv
   `pip install virtualenv`

2. Install python3: Download the latest Python 3 installer from the official Python website. Follow the installation instructions, and make sure to check the option to add Python to the PATH.
   `which python3`

3. Create a virtualenv in the project
   `virtualenv env`

4. Activate it: 

   * Before using the virtual environment, you'll need to activate it. In Windows, run `env\Scripts\activate`. On macOS and Linux, run `. env/bin/activate`. Your terminal or command prompt should now display the activated environment's name.

   * To deactivate the virtual environment, simply run `deactivate` in the terminal or command prompt.

5. Pip install Django and Django-rest-framework
   `pip install Django`
   `pip install djangorestframework`

6. Generate the requirements file
   `pip freeze > requirements.txt`

### Set up the Docker
1. Create a Dockerfile in the root of the project:
```dockerfile
FROM python:3.9

ENV PTYHONBUFFERED 1

RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/
```
2. Create the docker-compose.yml

```yml
version: '3.9'

services: 
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes: 
       - .:/to_delete
    ports:
      - "8000:8000"
```

### Set up the Project
1. With the virtualenv active, Create the Django project:
   `django-admin startproject server .`
   * Note: the extra . is important because we already have a project started
   These files can be re-generated.

2. Create the app:
   `python manage.py startapp src`

### Set up the Database
We're using postgres, not sqlite. Let's get a docker db running locally. 

1. Modify the docker-compose.yml to add:
```yml
  db:
    image: postgres:15.3
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=mys3cretpassw0rd!
      - POSTGRES_DB=restaurant
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
    pgdata:
```

2. Update requirements to add `psycopg2`
   `pip install psycopg2`
   `pip freeze > requirements.txt`

3. Update the settings.py file, add:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restaurant',
        'USER': 'postgres',
        'PASSWORD': 'mys3cretpassw0rd',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```
4. Build it!
`docker-compose up --build`