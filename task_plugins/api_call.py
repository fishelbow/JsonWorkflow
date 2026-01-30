import requests
import logging

TASK_TYPE = "api_call"

def run(task):
    url = task.get("url")
    method = task.get("method", "GET").upper()
    params = task.get("params", {})
    data = task.get("data", {})
    headers = task.get("headers", {})

    if not url:
        logging.error("api_call task missing 'url'")
        return False

    logging.info(f"API call: {method} {url}")

    try:
        if method == "GET":
            response = requests.get(url, params=params, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers)
        else:
            logging.error(f"Unsupported HTTP method: {method}")
            return False

        logging.info(f"Status: {response.status_code}")

        # Save the response JSON so other tasks can use it later
        try:
            task["output"] = response.json()
        except:
            task["output"] = response.text

        return True

    except Exception as e:
        logging.error(f"API call failed: {e}")
        return False