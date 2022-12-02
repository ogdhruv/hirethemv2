
<div align="center">

# Hire Them 🧑‍💻

    A web app to help colleges and their students.

</div>


### 🧪 Trying the deployed version:
- 🕵️ username: test  
- 🔑 password: letmetest

<ins> <h3> 🚧 The application is not mobile responsive right now. 🚧</h3> </ins>

##### _Made with :_

[![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://docs.djangoproject.com/) 
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/) 
[![PostgrSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/) 

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

##### _OS used :_

[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/) 

## 🌼 Features

- 👤 Custom User Model Authentication
- 📨 Integration with MailHog for local email testing
- 👥 A User Profile UI
- 💼 A Job Portal interface
- 💬 Room for Messaging or Chatting 
- 🧭 A fine and easy to understand frontend 
- 🗄️ Uses PostgreSQL database

## 📀 Installation!
<ins>**💯 _Recommendation : If you are using Windows kindly learn about [WSL](https://ubuntu.com/wsl)_**</ins>

🧭 _Follow all these step from **Prerequisite** to **Running this Project**:_

<details>
<summary>📖 Prerequisite</summary>

- Install 🐍 [Python3](https://www.python.org/) and [PIP](https://i.redd.it/ltidkb8taff61.jpg)
  - **alternative❓**- [Pyenv](https://github.com/pyenv/pyenv/)

- Install 🗄️ [PostgreSQL](https://www.postgresql.org/download/)
</details>
<details>
<summary>🗄️ PostgreSQL setup :</summary>

### 🗄️ PostgreSQL setup :

Setting up for **first time** user on linux :

[[click here ->](https://web.archive.org/web/20190303010033/http://suite.opengeo.org/docs/latest/dataadmin/pgGettingStarted/firstconnect.html)] 

- ***if getting ☣️ **ERROR**  like - Peer authentication failed for user "postgres"*** ([SOLUTION](https://stackoverflow.com/questions/69676009/psql-error-connection-to-server-on-socket-var-run-postgresql-s-pgsql-5432))

if you have already have used postgres, then just create database with project name:
            
            $ createdb --username=postgres hirethemv2

*  ✅ Important:
    
    * Either add this export:
        
            export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/<DB name given to createdb>
        in **bashrc or zshrc or Enviornment variable**.
    
    * or else add:

            export DJANGO_READ_DOT_ENV_FILE=True
        in **bashrc or zshrc or Enviornment variable**.Then you can create a `.env` file in root directory and add values there which is easy.
        
        First value to add in .env file is,
            
            export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/<DB name given to createdb>
        
</details>

### 👨‍🔧 Running this Project
1. Getting ready:
        
        $ git clone https://github.com/ogdhruv/hirethemv2.git
        $ cd hirethemv2
        $ virtualenv .venv
        $ source .venv/bin/activate
        $ pip install -r requirements/local.txt

1. Migrate the migrations to Postgres database:

        $ python manage.py migrate

2. Running the project:

        $ python manage.py runserver

## 📧 Using Email Backend

I have a user email verfication system in this project.

Right now it is set to "none" so you have to make it mendatory to use it.
    
1. Go to `config/settings/base.py`

2. On line `272`, change `ACCOUNT_EMAIL_VERIFICATION` from `"none"` to `"mendatory"`

3. In development, you use email catching tool for receiving email because you do have any SMTP service(like mailgun).
so we use an offline tool know as [**MailHog**](https://github.com/mailhog/MailHog).
    
    #### Setting up MailHog: 
    - Install latest MailHog release for your [OS](https://github.com/mailhog/MailHog) or [Ubuntu](https://github.com/mailhog/MailHog#debian--ubuntu-go--v118) <br/>
    - Run `$ ~/go/bin/MailHog` or else where you have go folder in the terminal.<br/>
    - Go to http://127.0.0.1:8025/ and check for emails when you create a user.<br/>

## ☁️ Testing Live

 😶‍🌫️ Few things to keep in mind
- Images may not appear on live becuase of disk space provided by render
- I

## 📚 Refrences and Books :
- [django-cookiecutter's Documentation](https://github.com/cookiecutter/cookiecutter-django)
- [LearnDjango](https://learndjango.com/tutorials/)
- [SIMPLE-IS-BETTER-THAN-COMPLEX](https://simpleisbetterthancomplex.com/)
- [FullStackPython](https://www.fullstackpython.com/django.html)
- [Django 4 By Example - Fourth Edition](https://www.amazon.in/Django-Example-powerful-reliable-applications/dp/1801813051)


## 🛸Deployment
- [hirethemv2](https://hirethemv2.onrender.com)
