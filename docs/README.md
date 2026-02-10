Workflow Engine Architecture Overview



Logging
A centralized logging system is configured at startup.
All engine components and plugins write to this unified logger.

Main Orchestrator
The main entry point coordinates the entire workflow lifecycle:
• 	Loads the workflow definition
• 	Resolves dependencies
• 	Executes tasks in the correct order
• 	Handles global error reporting

Core Engine Components
Plugin Loader
Discovers and imports task plugins dynamically from the plugin directory.
Task Registry
Stores plugin metadata and execution functions, making them available to the executor.
Task Runner
Validates tasks against plugin metadata and dispatches them to the correct plugin’s function.

Workflow Loader
- Reads workflow.JSON
- Validates structure
- Ensures each task has required fields
- Returns a normalized task list
Workflow Resolver
- Builds a dependency graph (DAG)
- Validates dependencies
- Produces a topologically sorted execution order
Workflow Executor
- Runs tasks in dependency‑safe order
- Uses the plugin system to execute each task
- Handles errors gracefully
- Stores outputs for downstream tasks

Workflow Pipeline
Loader
- Reads workflow JSON
- Validates structure
- Returns task list
Resolver
- Builds dependency graph
- Validates dependencies
- Produces execution order
Executor
- Runs tasks in order
- Uses plugin system
- Handles errors
- Stores outputs



Task Lifecycle
- Loaded from JSON
- Validated against plugin metadata
- Ordered by dependency resolution
- Executed by the Workflow Executor
- Output stored in task["output"]
- Used by dependent tasks




Next Steps Roadmap
The workflow engine is designed to be modular and extensible.
Upcoming enhancements will expand reliability, observability, and execution power.

🔹 Rotating Logs
Prevent log files from growing indefinitely.
Essential for long‑running workflows and production deployments.

🔹 Retries with Exponential Backoff
Automatically retry failed tasks with configurable:
• 	retry count
• 	delay
• 	backoff multiplier

🔹 Task Timeouts
Force‑fail tasks that hang or exceed a maximum runtime.

🔹 Task Outputs / Data Passing
Enhance the current  mechanism into a structured global context system.

🔹 Parallel Execution
Run independent tasks concurrently when dependencies allow.
Major performance boost for branching DAGs.

🔹 Workflow Scheduler
Run workflows automatically on a schedule (hourly, daily, weekly).
Transforms the engine into a lightweight orchestrator similar to Airflow or Prefect

🔹 Add some more test's.
Testing is new to me and it would be a great idea to get familair with the process.


