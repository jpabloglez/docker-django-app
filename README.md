# Django (DRF) learning project 


## Setup 
* Starting  from base_config branch
Run next commands:
```
docker-compose build
docker-compose up -d
```
After image is build and running
```
docker exec -it django-app django-admin startproject app
```
Once configured our project let's create our first django-app (users)
```
docker exec -it django-app bash 
cd app && python manage.py startapp users
```
Then apply migrations and create superuser
```
docker exec -it django-app bash 
cd app && python manage.py makemigrations 
python manage.py migrate
python manage.py cretesuperuser
```
## Setup 
* Starting from master or main/dev branch
Run next:
```
docker-compose build
docker-compose up -d
```
Create new django-app using:
```
docker exec -it django-app python manage.py migrate
```
