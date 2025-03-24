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

# how to reset the trame camera?
# todo: trame method call
# st.button("reset camera", on_click=reset_camera)

if "resolution" in st.session_state:
    res_val = st.session_state.resolution
else:
    res_val = 3

st.slider("Resolution", step=1, min_value=3, max_value=60, value=res_val, disabled=True)

st.checkbox("Select", key="select")

col1, col2 = st.columns(2)

with col1:
    st.write("trame-react iframe wrapper")
    trame_result = trame_app_iframe_wrapper(
        trame_app_url=trame_app_url,
        viewer_id="viewer1",

        # list of key to keep in sync from the trame world to the streamlit state
        sync_state_keys=[
            "interactor_settings",
            "resolution"
        ],
        # list of key to pass from the streamlit state to the trame world
        state={
            # "resolution": st.session_state.resolution,
            "interaction_mode": "select" if st.session_state.select else "interact",
        },
        key="persistent_viewer",
        height=500
    )

with col2:
    st.write("vanilla, regular iframe")
    components.iframe(trame_app_url, height=500)

if trame_result:
    new_resolution = trame_result["resolution"]

    if "resolution" not in st.session_state or st.session_state.resolution != new_resolution:
        st.session_state.resolution = new_resolution
        st.rerun()

    st.write("Resolution from React component:", trame_result['resolution'])
    st.write("Interactor settings from React component:", trame_result['interactor_settings'])
