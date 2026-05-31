# Importing Libraries
import json
from core.log import save_to_log
from pathlib import Path


def config_save(settings, filename="config.txt"):

    # Ensure the config directory exists
    config_directory = Path(__file__).resolve().parent
    config_directory.mkdir(parents=True, exist_ok=True)
    save_to_log("g", "Ensured that the config directory exists.")

    # Prepare the output path
    output_path = config_directory / filename
    save_to_log("g", "Preparing to save settings config.")

    # Save the settings to a JSON file
    try:
        with open(output_path, "w", encoding="utf-8") as config_file:
            json.dump(settings, config_file, indent=4)
        save_to_log("g", f"Settings config saved successfully to '{output_path}'.")
    except Exception as e:
        save_to_log("r", f"Failed to save settings config: {e}")

def config_load(filename="config.txt"):

    # Prepare the config file path
    config_directory = Path(__file__).resolve().parent
    config_path = config_directory / filename
 
    # Check if the config file exists
    if not config_path.exists():
        save_to_log("y", f"Config file '{config_path}' does not exist. Returning empty settings.")
        return {}
    
    # Load the settings from the JSON file
    try:
        with open(config_path, "r", encoding="utf-8") as config_file:
            data = json.load(config_file)
        save_to_log("g", f"Settings config loaded successfully from '{config_path}'.")
        return data
    except Exception as e:
        save_to_log("r", f"Failed to load settings config: {e}")
        return {}
