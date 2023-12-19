# Python example Microservice API

This repository contains an example Python application that you can use to test
out a microservice architecture.

In this case, the application serves out information on HTTP GET requests
regarding historical high and low temperatures for cities in Portugal. You can
use this API to connect it with other applications that can use this example
data.


## Setup the environment

Python is difficult to deal with regarding dependencies. Use a virtual
environment to set everything up, then activate it, and finally start the
application.


Create the virtual env

```
python3 -m venv .venv
```

Activate the environment

```
source .venv/bin/activate
```

Install the depencencies with the virtual environment activated

```
pip install -r requirements.txt
```


## Start the API

Use `uvicorn` to start the API

```
uvicorn --host 0.0.0.0 webapp.main:app
```

Inspect the running API at [http://0.0.0.0:8000](http://0.0.0.0:8000) after you
see the following output:

```
$ uvicorn --host 0.0.0.0 webapp.main:app
INFO:     Started server process [37770]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
