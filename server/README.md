# Setup
```
$ pip install --upgrade pip
$ pip install -r requirements.txt
$ pip install -e .
```

Fill __version__.py.

# RUN server
## Use flask built-in web server.
```
$ export FLASK_APP=flask_app
$ export FLASK_ENV=development
$ export FLASK_ROOT_PATH=<path to client dir>
$ cd <path to server/app dir>
$ flask run
```

## Use gunicorn.
Edit dot.env.development first. And then do the follow.
```
$ cd <path to server dir>
$ python gunicorn.py
```

## Run pytest.
```
$ cd <path to server dir>
$ pytest
```
