import streamlit as st
import streamlit_authenticator as stauth  # type: ignore
import yaml

from yaml.loader import SafeLoader

with open("assets/config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["pre-authorized"],
)

name, authentication_status, username = authenticator.login("main")  # type: ignore

if authentication_status:
    authenticator.logout("Logout", "main")  # type: ignore
    st.write(f"Welcome *{name}*")  # type: ignore
    st.session_state["username"] = username
    st.session_state["name"] = name
    st.switch_page("pages/task_page.py")
elif authentication_status == False:
    st.error("Username/password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password")
