# Micro Credit Application
## How to run:

Download or clone the reposatory:
```
git clone [REPO_URL]
```
Go to project folder:
```
cd [project folder]
```

Install Requirements Package:
```
pip install -r requirements.txt
```
Migrate Database:
```
python3 manage.py migrate
```
Create Super User:
```
python3 manage.py createsuperuser
```
Finally Run :
```
python3 manage.py runserver
```
It will start a local server on 'http://127.0.0.1:8000'

then go to http://127.0.0.1:8000/admin to accesss your administrations.
