# trame-streamlit - bridge from streamlit to trame

## Build
Built wheels will be available in the dist folder.

```bash
python -m venv .venv
source .venv/bin/activate
pip install build
python -m build .
```

## Example
The example is made of one trame application + three streamlit app.  
- `streamlit_to_trame.py` => streamlit app control the trame state
- `trame_to_streamlit.py` => trame state controls the streamlit app
- `bidirection.py` => mix of both world
Both the streamlit and trame applications needs to know the URL to each other.
```sh
cd example
python -m venv .venv
source .venv/bin/activate

# you need to install some trame related depencies + streamlit
pip install -r requirements.txt

# you need to install trame-streamlit
pip install ..

# run trame app
python ./trame-app/app.py --port 8081 --server --streamlit-origin http://localhost:8080

# open another terminal, make sure to activate the venv, then run streamlist
streamlit run streamlit_to_trame.py --server.port 8080 -- --trame-app-url http://localhost:8081
```
