import logging 
from workflow_loader import openJSON
from logging_config import setup_logging


def main():
    # configure logging at start of program run.

    setup_logging()
    logging.info("Ppogram started")

    workflow = openJSON()

    if workflow is None:
        logging.error("Workflow failed to load - exiting.")
        return

    # At this point, workflow is valid JSON
    logging.info("WorkFlow Loaded succesfully. Ready for next steps.")


    # Later:
    # run_workflow(workflow)

if __name__ == "__main__":
    main()


