# task_runner.py

import logging
import subprocess

def run_task(task):
    ttype = task.get("type", "print")

    if ttype == "print":
        return run_print_task(task)

    elif ttype == "shell":
        return run_shell_task(task)

    elif ttype == "python":
        return run_python_task(task)

    else:
        logging.error(f"Unknown task type: {ttype}")
        return False


def run_print_task(task):
    message = task.get("message", "")
    logging.info(f"[PRINT] {message}")
    return True


def run_shell_task(task):
    cmd = task.get("command")

    if not cmd:
        logging.error("Shell task missing 'command'")
        return False

    logging.info(f"[SHELL] Running: {cmd}")

    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Shell command failed: {e}")
        return False


def run_python_task(task):
    func_path = task.get("function")

    if not func_path:
        logging.error("Python task missing 'function'")
        return False

    logging.info(f"[PYTHON] Running function: {func_path}")

    try:
        module_name, func_name = func_path.rsplit(".", 1)
        module = __import__(module_name, fromlist=[func_name])
        func = getattr(module, func_name)
        func()
        return True
    except Exception as e:
        logging.error(f"Python function failed: {e}")
        return False