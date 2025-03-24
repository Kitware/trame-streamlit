import streamlit as st
import streamlit.components.v1 as components
from trame_streamlit import trame_app_iframe_wrapper
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "--trame-app-url",
    dest="trame_app_url",
    required=True,
    help="URL to use to reach trame",
    type=str,
)

args = parser.parse_args()
trame_app_url = args.trame_app_url

print(f"using {trame_app_url=}")

st.set_page_config(layout="wide")
st.title('Streamlit - trame Integration')

if "resolution" not in st.session_state:
    st.session_state.resolution = 12

st.slider("Resolution", step=1, min_value=3, max_value=60, key="resolution")

st.checkbox("Select", key="select")

col1, col2 = st.columns(2)

with col1:
    st.write("trame-react iframe wrapper")
    trame_app_iframe_wrapper(
        trame_app_url=trame_app_url,
        viewer_id="viewer1",

        # list of key to keep in sync from the trame world to the streamlit state
        # sync_state_keys=[],

        # list of key to pass from the streamlit state to the trame world
        state={
            "resolution": st.session_state.resolution,
            "interaction_mode": "select" if st.session_state.select else "interact",
        },
        key="persistent_viewer",
        height=500
    )

with col2:
    st.write("vanilla, regular iframe")
    components.iframe(trame_app_url, height=500)
