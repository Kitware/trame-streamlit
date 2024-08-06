import streamlit as st
import streamlit.components.v1 as components

from trame_app_component import trame_app_component

st.title('Streamlit - trame Integration')

if 'data' not in st.session_state:
    st.session_state.data = None

if 'resolution' not in st.session_state:
    st.session_state.resolution = 6 # Corresponds to the default resolution

data = trame_app_component(
    trame_app_url="http://localhost:8080",
    messages_to_trame=["streamlit-to-trame"],
    messages_to_streamlit=["trame_to_streamlit"],
)

if data and st.session_state.data != data:
    st.session_state.data = data
    st.session_state.resolution = int(data)

st.number_input("Resolution", step=1, min_value=3, max_value=60, key="resolution")

def send_message():
    post_value_message_content = f"{{ emit: 'streamlit-to-trame', value: {st.session_state.resolution} }}"

    js = f"""
    <script>
        parent.document.getElementsByTagName('iframe')[1].contentWindow.postMessage({post_value_message_content}, '*');
    </script>
    """
    components.html(js, height=0)

st.button("Send", on_click=send_message, args=())