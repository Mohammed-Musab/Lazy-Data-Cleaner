try:
    import json
    from pathlib import Path
except ImportError:
    print("Failed To Load Library [1]")

# Path Loader
try:
    config_directory = Path(__file__).resolve().parent.parent
    config_directory = config_directory / "user_data"
    config_directory.mkdir(parents=True, exist_ok=True)
    config_file = config_directory / "data.txt"
except Exception:
    print("Error occurred while setting up config directory [2, 1.1]")
    exit()


def config_save(settings, file=config_file):

    pass

def config_load(file=config_file):

    pass