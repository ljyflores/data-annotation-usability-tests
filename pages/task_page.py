import json
import os
import streamlit as st
import streamlit_authenticator as stauth  # type: ignore
import yaml
from yaml.loader import SafeLoader

# Get root path from session state
root_path = os.path.dirname(os.path.abspath(__file__)).strip("/pages")

# Authenticate
with open(f"assets/config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)
username, authentication_status, username = authenticator.login("main")
if authentication_status is None:
    st.switch_page("main.py")

# Show user metadata
username = st.session_state["username"]
task_metadata = json.load(open(f"assets/task_metadata.json", "r"))
user_metadata = json.load(open(f"data/{username}/user_metadata.json", "r"))

# Show tasks and progress in the captions
task_list = [task_metadata[task]["display_name"] for task in user_metadata.keys()]

caption_list = [
    f"Progress: {user_metadata[task]['completed_items']}/{user_metadata[task]['total_items']}"
    for task in user_metadata.keys()
]

selected_task = st.radio(
    "Select a Task", task_list, captions=caption_list, key="task_select_button"
)
st.session_state["using_shared_task"] = False

# Go to task
selected_key = list(user_metadata.keys())[task_list.index(selected_task)]
if st.button("Begin Task", key="task_begin_button"):
    st.switch_page(task_metadata[selected_key]["task_page"])
