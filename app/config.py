import yaml

def load_config():
    with open("config.yaml") as f:    #auto-closes the file (prevents leaks)
        return yaml.safe_load(f)      # Converts YAML → Python dict

config = load_config()