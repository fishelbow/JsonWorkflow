import logging
from .workflow_resolver import resolve_dependencies
from .workflow_executor import execute_tasks
from .task_runner import load_plugins
from .logging_config import setup_logging

def run_workflow(workflow_json: dict):
    setup_logging()
    load_plugins()

    logging.info("Workflow received via API")

    order = resolve_dependencies(workflow_json["tasks"])
    result = execute_tasks(order, workflow_json["tasks"])

    return result