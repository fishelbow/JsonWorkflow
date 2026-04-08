import logging
from src.engine.workflow_loader import open_JSON
from src.engine.logging_config import setup_logging
from src.engine.task_runner import load_plugins
from src.engine.core import run_workflow


# Local CLI entry point for the workflow engine
def main():
    # Configure logging
    setup_logging()
    logging.info("CLI started")

    try:
        # Load plugins
        load_plugins()
        logging.info("Plugins loaded")

        # Load workflow JSON from disk
        workflow = open_JSON()
        if workflow is None:
            logging.error("Workflow failed to load - exiting.")
            return

        logging.info("Workflow loaded successfully")

        # Run workflow through the engine
        result = run_workflow(workflow)
        logging.info(f"Workflow completed with result: {result}")

    except Exception as e:
        logging.exception(f"Fatal error in CLI: {e}")
        return


if __name__ == "__main__":
    main()
