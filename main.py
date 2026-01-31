import logging 
from engine.workflow_loader import open_JSON
from engine.logging_config import setup_logging
from engine.workflow_resolver import resolve_dependencies
from engine.workflow_executor import execute_tasks
from engine.task_runner import load_plugins


def main():
    # configure logging at start of program run.
    setup_logging()

    load_plugins() # --> plugins are added in the plugin folder and dynamically loaded 

    logging.info("Program started")

    workflow = open_JSON()

    if workflow is None:
        logging.error("Workflow failed to load - exiting.")
        return

    # At this point, workflow is valid JSON
    logging.info("WorkFlow Loaded succesfully. Ready for next steps.")


    # topology sort
    order = resolve_dependencies(workflow["tasks"])

    # tasks executed in order with regard to dependencies 
    execute_tasks(order, workflow["tasks"])

if __name__ == "__main__":
    main()



