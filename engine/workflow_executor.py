import logging
from engine.task_runner import run_task

def execute_tasks(order, tasks):
    logging.info("Beginning task execution")

    task_lookup = {task["id"]: task for task in tasks}

    for tid in order:
        task = task_lookup[tid]

        logging.info(f"Starting task: {tid}")

        success = run_task(task)

        if not success:
            logging.error(f"Task {tid} failed. Stopping workflow.")
            return False

        logging.info(f"Completed task: {tid}")

    logging.info("All tasks executed successfully")
    return True