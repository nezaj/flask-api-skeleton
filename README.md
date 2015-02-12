## Flask API Skeleton
Flask API Skeleton provides a bare-bones structure for a simple Flask API app.

### Quickstart
Because sometimes you just want to see it work
```
git clone git@github.com:nezaj/flask-api-skeleton.git
cd flask-api-skeleton
sudo pip install virtualenv
make virtualenv
source ~/.virtualenvs/flask-api-skeleton/bin/activate
./manage.py runserver
```

Now go to [http://localhost:5000/][localhost] in your favorite browser. Huzzah!

### Installing
You should build a [virtualenv][virtualenv] to contain this project's Python dependencies. The Makefile will create one for you and put it in `~/.virtualenvs/flask-api-skeleton`.
```
sudo pip install virtualenv
make virtualenv
```

Then activate it:
```
source ~/.virtualenvs/flask-api-skeleton/bin/activate
```

Instead of activating it manually like that, you might find it convenient to use [virtualenvwrapper][virtualenvwrapper] for working with virtualenvs:
```
sudo pip install virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh
workon flask-api-skeleton
```

If you ever need to upgrade it or install packages which appeared since your last run, just run `make virtualenv` again.

### Running
You can run the app using Flask's built-in Werkzeug development server via
```
./manage.py runserver
```

You may also specify the port and host like so:
```
./manage.py runserver --port=8080 --host=0.0.0.0  # listening on port 8080 to requests coming from any source
```

By default, the app runs using the `DevelopmentConfig` configuration defined in  the `settings` module. To point to a different configuration module, you can set the `CONFIG_ENV` variable:
```
CONFIG_ENV=test ./manage.py runserver
```

### Tests
The environment is preconfigured to contain [pep8][pep8] and [pylint][pylint], popular Python static analysis tools. [pytest][pytest] and [webtest][webtest] are also used for automated testing. You can run all the tests via `make check`

[localhost]: http://localhost:5000/
[pep8]: https://pypi.python.org/pypi/pep8
[pylint]: https://pypi.python.org/pypi/pylint
[pytest]: http://pytest.org/latest/contents.html
[secret-key]: http://flask.pocoo.org/docs/quickstart/#sessions
[sqlalchemy]: http://www.sqlalchemy.org/
[virtualenv]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org/en/latest/
[webtest]: http://webtest.readthedocs.org/en/latest/
