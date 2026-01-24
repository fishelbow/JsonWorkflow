import json
import logging 

def openJSON():
    data = None   # ensure data always exists, even if an exception happens

    try:
        # open and read JSON
        with open("workflow.json", "r") as jsonFile:
            data = json.load(jsonFile)

        # data is now a dictionary
        # data["tasks"] is a list of task dictionaries
 

    except FileNotFoundError:
        print("Error: workflow.json was not found. Check the file path.")

    except json.JSONDecodeError as e:
        print("Error: JSON is malformed:", e)

    except KeyError as e:
        print(f"Error: Missing expected key in JSON: {e}")

    except Exception as e:
        print("Unexpected error:", e)

    return data


def main():
    openJSON()


if __name__ == "__main__":
    main()