import json
import logging
from pathlib import Path
from typing import Generator, Union

logging.basicConfig(level=logging.INFO)

data_dir:Path = Path("./data")
json_files:Generator[Path, None, None] = data_dir.glob("*.json")

def get_type(attribute: Union[str, int, dict, list]):
    if isinstance(attribute, str):
        return "string"
    elif isinstance(attribute, int):
        return "integer"
    elif isinstance(attribute, list):
        # Check if values in array contains string
        if all([isinstance(element, str) for element in attribute]):
            return "enum"
        elif all([isinstance(element, dict) for element in attribute]):
            return "array"
    else:
        raise AttributeError(f"Attribute type not considered: {type(attribute)}")

def crawl_schema(message: dict, update_schema: dict):
    for key, value in message.items():

        if isinstance(value, dict):
            logging.info("Mapping found for key: %s...Recursing..." %key)
            crawl_schema(message[key], update_schema)
            continue

        key_schema = {
            "type": get_type(value),
            "tag": "",
            "description": "",
            "required": False,
        }
        if key in update_schema:
            logging.warning(f"\tkey: {key} found in update schema")
        update_schema[key] = key_schema

if __name__ == "__main__":
    for i, file_path in enumerate(json_files, start=1):
        with open(file_path, mode="r") as json_fp:
            logging.info(f"Reading file: {file_path.name}")
            data = json.load(json_fp)
        
        message = data["message"]
        message_schema = {}
        crawl_schema(message, message_schema)
        # logging.info(f"Schema 1: { message_schema.keys()}")

        schema_write_path = f"./schema/schema_{i}_test.json"
        with open(schema_write_path, mode="w") as f:
            json.dump(message_schema, f, indent=4)
            logging.info(f"Schema {i} saved: {schema_write_path}")
