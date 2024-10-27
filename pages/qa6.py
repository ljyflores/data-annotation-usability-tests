import json
import os
import time
import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth  # type: ignore
import yaml
from yaml.loader import SafeLoader
from typing import cast

# Load root path
root_path = os.path.dirname(os.path.abspath(__file__))

# Authenticate
with open(f"assets/config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["pre-authorized"],
)
name, authentication_status, username = authenticator.login()  # type: ignore
if authentication_status is None:
    st.switch_page("main.py")

# Load user data
username = st.session_state.username
data_path = f"data/{username}/qa6.csv"
metadata_path = f"data/{username}/user_metadata.json"

# Load task data and metadata
df = pd.read_csv(data_path)  # type: ignore
user_metadata = json.load(open(metadata_path, "r"))

# Identify unfinished reports
id_unfinished: list[object] = sorted(
    df.loc[(df["label"].isnull()) | (df["label"] == "")].index  # type: ignore
)
assert (
    len(id_unfinished)
    == user_metadata["qa6"]["total_items"] - user_metadata["qa6"]["completed_items"]
)


# Define a save function using the entered data
def save_data():
    with st.spinner("Selecting next annotation sample to show!"):
        time.sleep(30)

    # Retrieve the selected options
    report_idx = st.session_state.report_idx
    summary = getattr(st.session_state, f"qa_select_{report_idx}")

    # Save the selection in the dataframe
    df.loc[report_idx, "label"] = str(summary)

    # Update the metadata
    user_metadata["qa6"]["completed_items"] += 1

    # Save the data and metadata
    df.to_csv(data_path, index=False)
    with open(metadata_path, "w") as f:
        json.dump(user_metadata, f, indent=4)


next_button = st.button("Next", key="qa_next")
exit_button = st.button("Exit", key="qa_exit")

if next_button:
    report_idx = id_unfinished[0]

    # Display the report
    report_text = cast(str, df.loc[report_idx, "report"])  # type: ignore
    st.write(report_text)  # type: ignore

    with st.form(key="qa_form"):

        # Collect the annotation
        st.session_state.report_idx = report_idx
        options = st.text_area(
            label="Kindly provide the answer below",
            value="",
            key=f"qa_select_{report_idx}",
        )

        st.form_submit_button(label="Save", on_click=save_data)

if exit_button:
    # Return to main page
    st.switch_page("pages/task_page.py")
