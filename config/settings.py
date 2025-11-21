import json
import os

def load_environment(env):
    config_path = os.path.join("config", "environments.json")

    with open(config_path, "r") as f:
        data = json.load(f)

    if env not in data:
        raise ValueError(f"Environment '{env}' not found in environments.json")

    return data[env]["base_url"]
