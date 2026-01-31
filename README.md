

WORKFLOW ENGINE ARCITECTURE OVERVIEW 

logging configured 

main set as orchestrator of the workflow 

Plugin Loader — discovers and imports task plugins dynamically
Task Registry — stores plugin metadata and execution functions
Task Runner — validates tasks and dispatches them to the correct plugin


Workflow Loader — reads and validates the workflow JSON
Workflow Resolver — analyzes dependencies and determines execution order
Workflow Executor — runs tasks in the correct order using the plugin system

Here’s the full pipeline:
 Loader
 Reads workflow.JSON
 Validates structure
 Returns task list
 Resolver
 Builds dependency graph
 Validates dependencies
 Produces execution order
 Executor
 Runs tasks in order
 Uses plugin system
 Handles errors
 Stores outputs

JSON API contract

{
  "tasks": [ ... ]
}

id                  string          unique identifier for task
type                string          must match a plugins TASK_TYPE
depends_on          list(optional)  ids of task that must run first

Plugin Contract required 

TASK_TYPE           unique string       
run(task)           function            

Optional Plugin Metadata 

DESCRIPTION         string          
VERSION             string
REQUIRED_FIELDS     list of strings    fields the task must include in JSON
PARAM_SCHEMA        dict (optional)    future extension for type validation


######################### plugin example -- simple
import logging

TASK_TYPE = "print"
DESCRIPTION = "Prints a message to the log"
VERSION = "1.0"
REQUIRED_FIELDS = ["message"]

def run(task):
    message = task["message"]
    logging.info(f"[PRINT] {message}")
    return True


########################  

######################## plugin example -- complex

import requests
import logging

TASK_TYPE = "api_call"
DESCRIPTION = "Makes an HTTP request and stores the response"
VERSION = "1.0"
REQUIRED_FIELDS = ["url"]

def run(task):
    url = task["url"]
    method = task.get("method", "GET").upper()

    try:
        response = requests.request(method, url, **task.get("params", {}))
        task["output"] = response.json()
        return True
    except Exception as e:
        logging.error(f"API call failed: {e}")
        return False

####################################

A plugin is a Python module that defines TASK_TYPE, implements run(task), and optionally declares metadata like DESCRIPTION, VERSION, and REQUIRED_FIELDS so the engine can validate and execute tasks safely and consistently.


 

####################################### plugin registry structure 

# tasks loaded into registry for use in task execution

TASK_REGISTRY = {
    "<TASK_TYPE>": {
        "run": <callable>,
        "description": <string>,
        "version": <string>,
        "required_fields": <list>,
        "param_schema": <dict or None>
    }
}
#######################################

###################################### tasks output contract

# for using output from a task downstream 

task["output"] = <value>

##################################### 


Task Lifecycle
 Loaded from JSON
 Validated against plugin metadata
 Ordered by dependency resolution
 Executed by the Workflow Executor
 Output stored in task["output"]
 Used by dependent tasks


Plugin Error Handling
 Plugins should log errors instead of raising them
 The engine wraps run(task) in a try/except
 Plugins must return True on success, False on failure
 Failed tasks prevent dependent tasks from running

Together, these components form a modular, extensible workflow engine where new task types can be added simply by creating new plugins.


NEXT STEPS ROADMAP


The workflow engine is designed to be modular and extensible.
The following enhancements are planned to expand reliability, observability, and execution power:

🔹 Rotating Logs
Implement log rotation to prevent log files from growing indefinitely.
Useful for long‑running workflows and production deployments.

🔹 Retries with Exponential Backoff
Allow tasks to retry automatically when they fail.
Configurable retry count, delay, and backoff multiplier.

🔹 Task Timeouts
Prevent tasks from hanging forever.
Each task will have a maximum allowed runtime before being force‑failed.

🔹 Task Outputs / Data Passing
Enable tasks to pass data to downstream tasks.
This builds on the existing task["output"] contract and will evolve into a structured context system.

🔹 Parallel Execution
Run independent tasks concurrently when their dependencies allow it.
This will significantly speed up workflows with branching DAGs

🔹 Per‑Task Log Files
Each task will write to its own dedicated log file.
Improves debugging and isolates noisy plugins.

🔹 Workflow Scheduler
Allow workflows to run automatically on a schedule (hourly, daily, weekly, etc.).
This turns the engine into a lightweight orchestrator similar to Airflow or Prefect

