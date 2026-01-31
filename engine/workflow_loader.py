import json
import logging 

def open_JSON():
    data = None   # ensure data always exists, even if an exception happens

    try:

        logging.info("Attempting to load worflow.json")

        # open and read JSON
        with open("workflows/workflow.json", "r") as jsonFile:
            data = json.load(jsonFile)


        logging.info("workflow.json loaded successfully")
        logging.debug(f"Loaded keys: {list(data.keys())}")
        # data is now a dictionary
        # data["tasks"] is a list of task dictionaries
 

    except FileNotFoundError:
        logging.error("Error: workflow.json was not found. Check the file path.")

    except json.JSONDecodeError as e:
        logging.error("Error: JSON is malformed:", e)

    except KeyError as e:
        logging.error(f"Error: Missing expected key in JSON: {e}")

    except Exception as e:
        logging.error("Unexpected error:", e)

    return data

