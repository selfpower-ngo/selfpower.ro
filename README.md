# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###
Selfpower Website for Selfpower NGO at https://selfpower.ro

[![CircleCI](https://circleci.com/gh/selfpower-ngo/selfpower.ro.svg?style=svg)](https://circleci.com/gh/selfpower-ngo/selfpower.ro)
[![codecov](https://codecov.io/gh/selfpower-ngo/selfpower.ro/branch/develop/graph/badge.svg?token=vT8RIBSlb7)](https://codecov.io/gh/selfpower-ngo/selfpower.ro)
[![Python 3.7.7](https://img.shields.io/badge/python-3.6.7-blue.svg)](https://www.python.org/downloads/release/python-367/)
[![Django 2.2.13](https://img.shields.io/badge/django-2.0-blue.svg)](https://docs.djangoproject.com/en/2.1/releases/2.0/)

* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
Setup for local on Macbook, Staging and Live/Production.

* Deployment instructions

#### 0. Open a terminal window

#### 1. Make py3.6 virtualenv
Check if you have Py3 and ocally make a new virtualenv in myProjects:
```
# Go to you local projects folder:
cd $HOME/myProjects/
# Check to make sure Py3 is available:
which python3.6
/usr/local/bin/python3.6
# Create a virtualenv
python3 -m venv selfpower
```
#### Note: `rm pip-selfcheck.json` to remove it, because it is in the repo and will refuse to clone (Issue #196)

#### 2. Clone selfpower code from Github, repository into the previous virtualenv
Go to github to the selfpower repo, click the green button "Clone or download" to the repo link to clipboard:
```
cd selfpower
git clone --no-checkout git@github.com:ionescu77/selfpower.ro.git tmp && mv tmp/.git . && rmdir tmp && git checkout master
```

#### 3. Activate & install requirements
#### You need to add this ENV variables in your bin/activate file (later also in the `passenger_wsgi.py`):
- for local, staging, production

```
# activate:
export SECRET_KEY="blbabb32#%$@$#%$^$#^"
export DJANGO_SETTINGS_MODULE="SelfpowerProject.settings.local"

export MAILCHIMP_API="--hidden--"
export MAILCHIMP_LIST_ID="--hidden--"

export EMAIL_HOST_USER="webmaster@selfpower.ro"
export EMAIL_HOST_PASSWORD="--hidden--"

export GOOGLE_RECAPTCHA_SECRET_KEY="--hidden--"
export GOOGLE_RECAPTCHA_SECRET_SERVER_KEY="--hidden--"
```

- for staging and production also bear in mind `database_staging.py` and `database_production.py` need to read secrets from ENV Variables too, so you need this in activate:

```
export STAGING_DATABASE_PASSWORD="--hidden--"
```
- after adding those to `bin/activate`, finally we can activate the virtualenv

```
source bin/activate
# Check pip --version (must be 3.6)
pip --version
# Install requirements
pip install -r requirements/local.txt
```

#### Note that today due to #190 we need to check for the 0.9.6 version of this:
```
pip install django-markdown-app==0.9.6
```

- for passenger_wsgi.py variables should be set like this:

```
os.environ['DJANGO_SETTINGS_MODULE'] = "SelfpowerProject.settings.test"
os.environ['SECRET_KEY'] = ")&mx2e#kxcjitqcke^+1ji1-wk#m47sd9crs4!bstnk)*8u@"
os.environ['EMAIL_HOST_USER'] = 'webmaster@selfpower.ro'
os.environ['EMAIL_HOST_PASSWORD']="--hidden--"
os.environ['GOOGLE_RECAPTCHA_SECRET_KEY']='--hidden--'
os.environ['GOOGLE_RECAPTCHA_SECRET_SERVER_KEY']='--hidden--'
os.environ['MAILCHIMP_API']="--hidden--"
os.environ['MAILCHIMP_LIST_ID']="--hidden--"
os.environ['STAGING_DATABASE_PASSWORD']='--hidden--'
```

#### 4. Migrate
```
python src/manage.py makemigrations

python src/manage.py migrate
```

#### 5. setup admin user
```
python src/manage.py createsuperuser
Nume utilizator (leave blank to use 'razvansky'):
Adresă de email: some_email@mail.raz
Password:
Password (again):
created post_save 8hfg2o3gpefh3go2fjwurygt3984fhibwi   razvansky
Superuser created successfully.
```
It is not the case because the sqlite was still in the repo

#### 6. Start server and initialize profiles
```
python src/manage.py runserver
```

#### Important Note
Before accessing the last menu item [user profile](http://127.0.0.1:8000/autentificare/profile/)!

http://127.0.0.1:8000/autentificare/profile/

You need to login one first time in [Administrare](http://127.0.0.1:8000/administrare) - the Administrative Web Interface - in order to create the first profile:

http://127.0.0.1:8000/administrare

For the example login with the superuser.
Otherwise you will get a crash when accessing the profile page.

## Contributors

- [![](https://github.com/alexinntekt.png?size=50)](https://github.com/AlexInntekt)
- [![](https://github.com/ionescu77.png?size=50)](https://github.com/ionescu77)

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
