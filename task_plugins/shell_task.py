import logging
import subprocess

TASK_TYPE = "shell"

def run(task):
    cmd = task.get("command")
    if not cmd:
        logging.error("Shell task missing 'command'")
        return False

    logging.info(f"[SHELL] Running: {cmd}")

    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except Exception as e:
        logging.error(f"Shell command failed: {e}")
        return False