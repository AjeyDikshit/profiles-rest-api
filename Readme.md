# Django project steps:

### Setup:
- Create a virtual environment using: (This will create a virtual environment in cwd)
``` bash
python -m venv <environment name>
```
- Activate the virtual environment:
```bash
./<environment name>/Scripts/activate
```
- Install required packages: django, djangorestframework

### Creating a new project
- Start a project:
```bash
django-admin startproject <project name> <path for project> 
```
- Start an app: This will create also create a new folder with ```<app name>``` name which will include all the required files
```bash
python manage.py startapp <app name>
```



### Models:
- Models are used in Django to describe the data we need for our application.
- Django uses these models to set up and configure our database to store our data effectively.
- Django handles the relationship between our models and the database for us so we never need to write any SQL statements or interact with the database directly.
