import argparse
import json
import os
import pandas as pd
import shutil

tasks_to_assign = ["qa1", "qa2", "qa3", "qa4", "qa5", "qa6"]

parser = argparse.ArgumentParser()
parser.add_argument("--username", type=str, required=True)
args = parser.parse_args()

if not os.path.exists(f"data/{args.username}"):
    os.mkdir(f"data/{args.username}")
if not os.path.exists(f"data/{args.username}/user_metadata.json"):
    user_metadata = {}
else:
    user_metadata = json.load(open(f"data/{args.username}/user_metadata.json", "r"))

for task_name in tasks_to_assign:
    if not os.path.exists(f"data/{args.username}/{task_name}.csv"):
        shutil.copyfile(f"raw/{task_name}.csv", f"data/{args.username}/{task_name}.csv")
        total_items = len(pd.read_csv(f"raw/{task_name}.csv"))  # type: ignore

        user_metadata[task_name] = {"completed_items": 0, "total_items": total_items}
        with open(f"data/{args.username}/user_metadata.json", "w") as f:
            json.dump(user_metadata, f, indent=4)
    else:
        assert False, "Task already exists! Not doing anything to prevent overwriting"
