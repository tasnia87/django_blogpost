# django_blogpost
Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern.Being a Python Web framework, Django requires Python. 
In this project I have build a simple blog application where the basic features are included.
## Features
* User Authentication
* Create new post
* Update Post
* Delete Post
* View post details
## Installation
See What [Python version](https://docs.djangoproject.com/en/3.2/faq/install/#faq-python-version-support) can I use with Django? for details. Python includes a lightweight database called [SQLite](https://www.sqlite.org/index.html) so you won’t need to set up a database just yet.
Install [django](https://docs.djangoproject.com/en/3.2/topics/install/#installing-official-release) from here.


## Getting Started
For this project I have installed django version 2.1 and python version 3.7.
## For creating project directory
```bash
$ django-admin startproject django_project
```
Then we have to open that directory into a editor
```bash
$ cd django_project
```
## For start and manage project
```bash
$ python manage.py startapp blog
```
## Development of Server
For running the server
```bash
$ python manage.py runserver
```
Navigate to http://localhost:8000/blog. This will take you to the home page.

## Admin Login
```bash
$ python manage.py makemigrations # updates the changes in databases
$ python manage.py migrate # run through some migrations
$ $ python manage.py createsuperuser # It will enable to login the admin. An email and password must be included in order to admin login.
```
### Creating database tables for creating 'New Post'
In 'blog' app django has already created a models.py file. In models.py file we have created tables for posts. After making post tables model we have run makemigrations command as mentioned before which made the changes done and ./manage.py migrate command to save that.
### For more help visit [django](https://docs.djangoproject.com/en/3.2/)

## Download project and Run
### Using Git (recommended)
Navigate & Clone this project (will be cloned inside myProject folder) using this command.
```bash
git clone https://github.com/tasnia87/django_blogpost ./myProject
```
### Using manual download ZIP
- Download repository
- Extract the zip file, navigate into it & copy the folder to your desired directory

