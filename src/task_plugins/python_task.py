import logging

TASK_TYPE = "python"
DESCRIPTION = "Imports and executes a Python function"
VERSION = "1.0"
REQUIRED_FIELDS = ["function"]

def run(task):
    func_path = task.get("function")
    if not func_path:
        logging.error("Python task missing 'function'")
        return False

    try:
        module_name, func_name = func_path.rsplit(".", 1)
        module = __import__(module_name, fromlist=[func_name])
        func = getattr(module, func_name)
        func()
        return True
    except Exception as e:
        logging.error(f"Python function failed: {e}")
        return False