try:
    import json
    from pathlib import Path
except ImportError:
    print("Failed To Load Library [1]")

def config_save(settings, filename="config.txt"):

    # Ensure the config directory exists
    config_directory = Path(__file__).resolve().parent
    config_directory.mkdir(parents=True, exist_ok=True)

def config_load(filename="config.txt"):

    # Prepare the config file path
    config_directory = Path(__file__).resolve().parent
    config_path = config_directory / filename