# todo-app
A TODO app, which sets up to-do lists for its users

* [Link](https://www.toptal.com/python/build-high-performing-apps-with-the-python-fastapi-framework)

## Features
* Signup and Login
* Add new TODO item
* Get a list of all TODOs
* Delete/Update a TODO item

## Installation
### Create virtual environment

``virtualenv fvenv -p python3.X``
### Activate virtual environment

``source fvenv/bin/activate``

### Install dependencies
``pip install -r requirements.txt``

### Copy and populate env variables
cp .env.example .env
```

Edit .env file to define
```vim
DATABASE_URL='sqlite:///./todo.db'
```

### Run the project 
``uvicorn main:app --reload --host 0.0.0.0 --port 8000``