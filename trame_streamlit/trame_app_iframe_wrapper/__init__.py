import streamlit.components.v1 as components
import os

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/dist")

trame_app_iframe_wrapper = components.declare_component(
    "trame_app_iframe_wrapper",
    path=build_dir
)
