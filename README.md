# Template for Vue-Flask CRUD Web application

This is a template to build web application with Vue.js for Frontend, Python Flask for backend, and Gunicorn as WSGI.

## Requisites
In order to use this template, you'll need to have the follows.
* Python3
* npm
* node (required for npm)

For setting up python3, use of virtualenv is recommended.<br>
[Here](https://github.com/daichi-yoshikawa/python-boilerplate) is one of instructions for virtualenv(See (Option2) Create virtualenv).

As for npm (and node), [here](https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/) is a great instruction.

## Get Started

Firstly, do the follows with one terminal. This is to bundle/compile client scripts(html, css, js, vue). The resulting files will be generated in client/dist/dev dir.
```
$ git clone https://github.com/daichi-yoshikawa/vue-flask-boilerplate
$ cd <path-to-vue-flask-boilerplate>
$ cd client
$ npm install
$ npm
```

And then, do the follows with another terminal.
```
$ cd <path-to-vue-flask-boilerplate>
$ cd server
```
If you use pyenv and pyenv-virtualenv, do the follows to set python virtualenv to the directory.
```
$ pyenv install <version of python(Eg. 3.7.6)>
$ pyenv virtualenv <version of python(Eg. 3.7.6)> <venv name(Eg. py376-webapp)>
$ cd <path-to-vue-flask-boilerplate>/server
$ pyenv local <venv name(Eg. py376-webapp)>
```
And run python file under server dir.
```
$ python gunicorn.py
```

Now you can check if everything is going well by opening browser and input "localhost:5000" in URL bar. You'll see like below.

## How to extend code
### Backend (Flask)
#### Add more routes
#### Add more APIs
#### Add more DB tables
#### Add more DBs

### Frontend (Vue.js)
#### Add more 3rd party js files
#### Add more your own js files
#### Add more Vue components
#### Add more Vue routes
