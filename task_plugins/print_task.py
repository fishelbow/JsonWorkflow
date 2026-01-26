import logging

TASK_TYPE = "print"

def run(task):
    message = task.get("message", "")
    logging.info(f"[PRINT] {message}")
    return True