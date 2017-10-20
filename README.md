# Bundesliga website
Website that gives information about Bundesliga games. It is written in Python 3.5.2 using Django and storing data in mysql database.

## Instructions to run the application (on Linux):
It is recommended to use virtual environment to seperate working environments for different applications. Create a virtualenv for the bundesliga application (lets say that ~/.virtualenvs is the directory for virtual environments):
```
cd ~/.virtualenvs/
mkdir bundesliga
cd bundesliga/
virtualenv --system-site-packages .
```
Enter in the virtual environment:
```
. ~/.virtualenvs/bundesliga/bin/activate
```
If you don't have mysql server, install it. Username and password for testing purposes are 'root' and 'test', you may change it in django settings:
```
sudo apt install mysql-server
```
Install application dependencies (from now on, we are working in the django_bundesliga directory):
```
pip install -r requirements.txt
```
Enter mysql and create database called 'bundesliga':
```
mysql -u USER -pPASSWORD
CREATE DATABASE bundesliga
```
Migrate the database:
```
python manage.py migrate
```
If everything so far is okay, then run the application:
```
python manage.py runserver
```
and you can open it in web browser at:
```
http://localhost:8000/bundesliga_app
```
Hopefully you will see all matches for First Bundesliga for this season.
