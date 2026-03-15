import logging

TASK_TYPE = "print"
DESCRIPTION = "Prints a message to the log"
VERSION = "1.0"
REQUIRED_FIELDS = ["message"]


def run(task):
    message = task.get("message", "")
    logging.info(f"[PRINT] {message}")
    return True