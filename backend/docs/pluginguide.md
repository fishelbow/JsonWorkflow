Plugin Authoring Guide
This guide explains how to create new task plugins for the Workflow Engine.
Plugins allow you to extend the engine with new task types simply by adding Python modules to the plugins/ directory.
A plugin is just a Python file that defines a few required variables and implements a run(task) function. The engine discovers plugins automatically — no registration code required.


Plugin Basics
Every plugin must define:

Name:          Required:    Description:

TASK_TYPE       yes        Unique string identifying the task type
run(task)       yes        Function that performs the task and returns True or False
DESCRIPTION     no         Human-readable explanation 
VERSION         no         Plugin version string
REQUIRED_FIELDS no         List of JSON fields the task must include
PARAM_SCHEMA    no         Future extension for type validation 

The engine loads these attributes dynamically and stores them in the Task Registry.

a plugin is a single Python file inside the task_plugins/ directory:

task_plugins/
│
├── __init__.py
├── api_call.py
├── print_task.py
├── python_task.py
├── shell_task.py
└── your_new_plugin.py   ← create this

Each file corresponds to task type

Minimal Plugin Example

This is the smallest valid plugin:

TASK_TYPE = "hello_world"

def run(task):
    print("Hello from plugin!")
    return True

This plugin requires no fields and always succeeds

Plugin With Metadata

Metadata helps the engine validate tasks and improves documentation.

import logging

TASK_TYPE = "print"
DESCRIPTION = "Prints a message to the log"
VERSION = "1.0"
REQUIRED_FIELDS = ["message"]

def run(task):
    logging.info(f"[PRINT] {task['message']}")
    return True

The engine will:
- ensure "message" exists in the JSON
- pass the entire task dict to run(task)
- log the output


Complex Plugin Example

Plugins can perform network calls, file operations, or anything else Python can do

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

   This plugin:
- validates that "url" is present
- performs an HTTP request
- stores the response in task["output"]
- returns success/failure


Returning output

Plugins can pass data to downstream tasks by writing to:

task["output"] = <any value>

Downstream tasks can access this via dependency resolution.
Example:

task["output"] = {"status": "ok", "value": 42}

Error Handling Rules

To keep the engine stable:
• 	Plugins should not raise exceptions
They should catch errors internally and log them.
• 	Plugins must return  or 
• 	 → task succeeded
• 	 → task failed and dependents will not run
• 	Use logging instead of print
The engine manages logging globally.
Example:

try:
    ...
except Exception as e:
    logging.error(f"My plugin failed: {e}")
    return False


    Accessing Task fields

  The task argument is a dictionary containing:
- all fields from the workflow JSON
- any fields added by upstream plugins (e.g., task["output"])
Example:

  value = task.get("value", 0)

  Testing Your Plugin

  You can test a plugin manually:

  from plugins.my_plugin import run

task = {
    "id": "test",
    "type": "my_plugin",
    "foo": "bar"
}

run(task)

Or run it through a workflow JSON to test dependency behavior

Best Practices

1. Keep plugins small and focused
One plugin = one task type.
2. Validate inputs early
Use REQUIRED_FIELDS to enforce correctness.
3. Log everything important
Errors, warnings, and key actions.
4. Avoid global state
Plugins should be stateless and idempotent.
5. Use task["output"] consistently
Downstream tasks depend on predictable structure.
6. Fail gracefully
Return False instead of raising exceptions.


Advanced Plugin Feature (Future)

The engine roadmap includes:
- PARAM_SCHEMA for type validation
- per‑task log files
- retries and backoff
- timeouts
- parallel execution
- shared context object
Plugins will automatically benefit from these enhancements as the engine evolves

