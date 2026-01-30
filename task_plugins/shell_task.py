import logging
import subprocess

TASK_TYPE = "shell"
DESCRIPTION = "Runs a shell command"
VERSION = "1.0"
REQUIRED_FIELDS = ["command"]

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