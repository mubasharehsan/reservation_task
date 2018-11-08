Dynamo application
==================

Major Requirements:
:   -   Python3.5

API docs can be found at: [docs](<https://documenter.getpostman.com/view/3592529/RzZ7ofvD>)
---------------------------------------------------------------------

First, create a virtual environment and install requirements (Make sure
you've installed python3.5):

``` {.sourceCode .bash}
virtualenv -p python3.5 ~/.virtualenvs/dynamo
source ~/.virtualenvs/dynamo/bin/activate
cd dynamo
pip install -r requirements.txt
```

Now put the user-name and pasword to settings.py file in DATABASES
configurations.

Run migrations:

``` {.sourceCode .bash}
python manage.py migrate
```

Create a superuser to access Django Administration Console (i.e.
/admin):

``` {.sourceCode .bash}
python manage.py create_admin # This will also print superuser credentials.
```

Finally, run development server as follow:

``` {.sourceCode .bash}
python manage.py runserver 0.0.0.0:8000
```

Now, you will be able to visit Juntos @ <http://localhost:8000> and
Django Admin @ <http://localhost:8000/admin/>

To clean environment following commands can be used:

``` {.sourceCode .bash}
deactivate
rm -rf ~/.virtualenvs/dynamo
find . -name "*.pyc" -exec rm -f {} ;
```
