import logging
import importlib
import pkgutil
import task_plugins

TASK_REGISTRY = {}

def load_plugins():
    logging.info("Loading task plugins...")

    for _, module_name, _ in pkgutil.iter_modules(task_plugins.__path__):
        module = importlib.import_module(f"task_plugins.{module_name}")

        task_type = getattr(module, "TASK_TYPE", None)
        run_func = getattr(module, "run", None)

        if not task_type:
            logging.error(f"Plugin {module_name} missing TASK_TYPE")
            continue

        if not run_func:
            logging.error(f"Plugin {module_name} missing run() function")
            continue

        TASK_REGISTRY[task_type] = {
            "run": run_func,
            "description": getattr(module, "DESCRIPTION", "No description provided"),
            "version": getattr(module, "VERSION", "0.1"),
            "required_fields": getattr(module, "REQUIRED_FIELDS", []),
            "param_schema": getattr(module, "PARAM_SCHEMA", None),  # optional future feature
        }

        logging.info(f"Registered task type: {task_type}")


def run_task(task):
    ttype = task.get("type")
    meta = TASK_REGISTRY.get(ttype)

    if not meta:
        logging.error(f"Unknown task type: {ttype}")
        return False

    # Validate required fields
    for field in meta["required_fields"]:
        if field not in task:
            logging.error(f"Task '{task.get('id')}' missing required field: {field}")
            return False

    # Execute plugin safely
    try:
        return meta["run"](task)
    except Exception as e:
        logging.error(f"Task '{task.get('id')}' failed: {e}")
        return False