import argparse
import streamlit_authenticator as stauth  # type: ignore
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("--username", type=str, required=True)
parser.add_argument("--password", type=str, required=True)
parser.add_argument("--email", type=str, required=False, default=None)
parser.add_argument("--name", type=str, required=False, default=None)
args = parser.parse_args()

with open("assets/config.yaml", "r") as file:
    config = yaml.safe_load(file)

if args.username in config["credentials"]["usernames"]:
    raise ValueError("Username already taken!")

config["credentials"]["usernames"][args.username] = {
    "email": args.email,
    "name": args.name,
    "password": str(stauth.Hasher([args.password]).generate()[0]),  # type: ignore
}

with open("assets/config.yaml", "w") as file:
    yaml.dump(config, file)
