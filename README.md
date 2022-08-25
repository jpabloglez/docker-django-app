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
docker exec -it django-app python manage.py startproject
```
Once configured our project
```
docker exec -it django-app python manage.py makemigrations 
docker exec -it django-app python manage.py migrate
docker exec -it django-app python manage.py cretesuperuser
```
## Setup 
* Starting from master or dev branch
Run next:
```
docker-compose up -d
```
