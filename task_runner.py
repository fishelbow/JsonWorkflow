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

        if task_type and run_func:
            TASK_REGISTRY[task_type] = run_func
            logging.info(f"Registered task type: {task_type}")
        else:
            logging.warning(f"Plugin {module_name} missing TASK_TYPE or run()")

def run_task(task):
    ttype = task.get("type")
    func = TASK_REGISTRY.get(ttype)

    if not func:
        logging.error(f"Unknown task type: {ttype}")
        return False

    return func(task)