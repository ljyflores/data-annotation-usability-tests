import argparse
import json
import os
import pandas as pd
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("--username", type=str, required=True)
parser.add_argument("--task", type=str, required=True)
args = parser.parse_args()

if not os.path.exists(f"data/{args.username}"):
    os.mkdir(f"data/{args.username}")
    user_metadata = {}
else:
    user_metadata = json.load(open(f"data/{args.username}/user_metadata.json", "r"))

if not os.path.exists(f"data/{args.username}/{args.task}.csv"):
    shutil.copyfile(f"raw/{args.task}.csv", f"data/{args.username}/{args.task}.csv")
    total_items = len(pd.read_csv(f"raw/{args.task}.csv"))  # type: ignore

    user_metadata[args.task] = {"completed_items": 0, "total_items": total_items}
    with open(f"data/{args.username}/user_metadata.json", "w") as f:
        json.dump(user_metadata, f, indent=4)
else:
    assert False, "Task already exists! Not doing anything to prevent overwriting"
