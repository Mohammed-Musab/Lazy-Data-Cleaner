try:
    import json
    from pathlib import Path
except ImportError:
    print("Failed To Load Library [1]")

# Path Loader

try:
    config_directory = Path(__file__).resolve().parent.parent
    config_directory = config_directory / "user_data" / "data.txt"
    config_directory.mkdir(parents=True, exist_ok=True)
except Exception:
    print("Error occurred while setting up config directory [2, 1.1]")

def config_save(settings, filename="config.txt"):

    pass

def config_load(filename="config.txt"):

    # Prepare the config file path
    config_directory = Path(__file__).resolve().parent
    config_path = config_directory / filename