# README #

This README would normally document whatever steps are necessary to get your application up and running.

### Dependencies ###

* Python 3.x
* PostGreSQL 9.x


### Getting Started ###

* Create a user for postgres : "createuser tribe --pwprompt --superuser"
* Set password for the user : <DB_PASSWORD>
* Create a db for the application : "createdb userss"


### Virtual Environment Setup ###

* Setup  virtualenv : "virtualenv -p python3 env"
* Move to virtualenv and activate its environment


### Dependency Setup ###

* Install requirements: "pip install -r requirements.txt".
* In settings.py, change <DB_PASSWORD>
* Run migrations: "python manage.py migrate"
* Create superuser: "python manage.py createsuperuser"





