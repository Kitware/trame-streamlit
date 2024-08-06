# Streamlit/trame application 

Requires a paraview 5.10+

## Virtual environment

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## trame application

### Run trame-app
```sh
cd trame-app
path/to/pvpython ./app.py --port 8080 --server --venv absolute/path/to/.venv
```

## Streamlit Application

### Setup

In case the trame application is not running on http://localhost:8080, then modify the iframe source URL in ./streamlit/app.py file when instanciating trame_app_component() by changing the trame_app_url value.

In an other terminal:

```sh
source ./venv
streamlit run ./streamlit/app.py --server.port 8081
```

### Apps communication
Before launching the streamlit app, please modify
.venv/lib/python3.9/site-packages/trame_iframe/module/serve/trame-iframe.umd.js file:

Change in "Communicator" section:

```sh
window.postMessage(e,"*");
```

by

```sh
window.parent.postMessage(e,"*");
```

Open localhost:8081 on your web browser