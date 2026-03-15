

JSON API Contract

A workflow JSON file defines a list of tasks to be executed by the Workflow Engine.
The top‑level structure must contain a single key:


{
  "tasks": [...]
}

Name:                     Type:              Required:     Description:

id                        string                yes         Unique identifier for the task
type                      string                yes         Must match a plugin's TASK_TYPE
depends_on                list                  no          IDs of tasks that must run first
Plugin-specific fields    varies                no          Additional fields required by the plugin

Example Task Object
Here is a correct example of a task definition


{
  "id": "run_python",
  "type": "python",
  "depends_on": ["list_files"],
  "function": "tasks.sample_function"
}

 This task:
- has an ID (run_python)
- uses the python plugin
- depends on the task list_files
- includes a plugin‑specific field (function)

Example Workflow structure

{
  "tasks": [
    {
      "id": "list_files",
      "type": "shell",
      "command": "dir"
    },
    {
      "id": "run_python",
      "type": "python",
      "function": "tasks.sample_function",
      "depends_on": ["list_files"]
    }
  ]
}

Validation Rules
The Workflow Loader enforces:
Required Fields
- id must be present and unique
- type must match a known plugin
- plugin‑specific REQUIRED_FIELDS must be present
Dependency Rules
- depends_on must reference valid task IDs
- no circular dependencies allowed
Structure Rules
- tasks must be an array
- each task must be an object



