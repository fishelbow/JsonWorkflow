Workflow Project

Workflow project
Part 1:
Simple Python Workflow

Project Overview:
You will create a small Python program that reads a workflow from a JSON file and executes each task in the correct order. Tasks may depend on other tasks, and your program should respect these dependencies. By the end, you'll understand basic workflow orchestration and dependency management.


Step-by-Step Checklist:
✅ Step 1: Load the workflow JSON

Read a JSON file into Python using the JSON module.
Store tasks in a dictionary or list.
✅ Step 2: Understand task dependencies

Each task can depend on zero or more other tasks.
Make sure your program can check if all dependencies of a task are complete.
✅ Step 3: Determine execution order

Identify tasks that are ready to run (all dependencies finished).
Implement a simple topological sort or loop-based method to decide order.
✅ Step 4: Execute tasks

For now, tasks can be simple: print a message, do a calculation, or run a small function.
Mark tasks as completed once they run.
✅ Step 5: Logging

Print which task is starting and which finishes.
Show friendly error messages for missing dependencies.
✅ Step 6 (Optional stretch): Handle errors

Detect cycles in the workflow and print an error.
Skip or retry failed tasks (advanced).

Key Ideas & Skills to Master by the End:
JSON Handling:
Read, parse, and access data from JSON files in Python.
Dependencies & DAGs:
Understand what a Directed Acyclic Graph is.
Know how dependencies affect the execution order of tasks.
Topological Sorting / Execution Order:
Be able to figure out which tasks can run first.
Understand that a task can only run after all its dependencies are complete.
Task Execution:
Run simple Python functions as tasks.
Keep track of which tasks are finished.
Error Handling & Logging:
Print clear logs of what’s running.
Handle missing dependencies and detect potential cycles.
Problem-Solving & Debugging:
Break down the workflow into steps.
Check intermediate results and logs to debug execution order issues.

Example JSON Input:
{

  "tasks": [

    {"id": "task1", "type": "print", "message": "Hello"},

    {"id": "task2", "type": "print", "message": "World", "depends_on": ["task1"]},

    {"id": "task3", "type": "print", "message": "Done!", "depends_on": ["task2"]}

  ]

}


Perfect! Here’s a junior-to-intermediate-friendly project description for a visual workflow JSON builder using React Flow, designed to complement the Python workflow engine.


Part 2 :
Visual Workflow JSON Builder with React Flow (JavaScript)


Project Overview:
This project is about creating a visual tool that allows users to design workflows as a graph of tasks using drag-and-drop. Each node represents a task, and connections represent dependencies. Once the workflow is designed, the tool outputs a JSON file compatible with the Python workflow engine from the first project.

This project will teach you React basics, working with libraries like React Flow, state management, and JSON generation.


Objectives:
Visual Workflow Builder:
Use React Flow to create a canvas where users can add, move, and connect nodes.
Each node represents a task with customizable properties (task ID, type, message, etc.).
Task Dependencies:
Connections between nodes indicate which tasks depend on others.
Prevent cycles or visually warn the user if a cycle is created.
JSON Output:
Generate a JSON object that matches the format the Python workflow engine expects.
Allow users to download or copy the JSON.
Basic UI Features:
Add new tasks (nodes) to the canvas.
Edit task properties via a simple form.
Delete tasks or connections.
Zoom and pan the workflow canvas.

Example Output JSON:
{

  "tasks": [

    {"id": "task1", "type": "print", "message": "Hello"},

    {"id": "task2", "type": "print", "message": "World", "depends_on": ["task1"]},

    {"id": "task3", "type": "print", "message": "Done!", "depends_on": ["task2"]}

  ]

}



Step-by-Step Checklist for Implementation:
✅ Step 1: Setup React App

Use Create React App or Vite.
Install React Flow (npm install react-flow-renderer).
✅ Step 2: Basic Canvas

Display a React Flow canvas.
Add zoom and pan functionality.
✅ Step 3: Add Nodes

Create a button or menu to add new task nodes.
Each node should have a unique ID and task type.
✅ Step 4: Connect Nodes

Allow users to draw edges between nodes.
Track which nodes depend on which other nodes.
✅ Step 5: Edit Node Properties

Show a simple form when a node is selected.
Allow editing task type, message, or other properties.
✅ Step 6: Generate JSON

Convert the visual graph into a JSON object like the Python workflow engine expects.
Include task IDs, types, messages, and depends_on arrays.
✅ Step 7: Export JSON

Add a button to download the JSON or copy it to the clipboard.
✅ Step 8 (Optional Stretch): Validation

Detect cycles and show warnings.
Validate that task IDs are unique.

Key Ideas & Skills to Master by the End:
React Basics:
Functional components, state (useState), and props.
Handling events and forms.
React Flow:
Nodes, edges, and layout.
Adding/removing nodes and connections dynamically.
State Management:
Keeping track of nodes, edges, and their properties.
Updating dependencies when edges are added/removed.
JSON Generation:
Converting a graph structure into a standard JSON format.
Ensuring dependencies are correctly represented.
UI/UX Considerations:
Make the interface intuitive for adding/editing tasks.
Handle errors like duplicate task IDs or cycles gracefully.
Integration:
Output JSON that can directly feed the Python workflow engine from the first project.

This project can pair perfectly with the Python workflow engine: one builds workflows visually in React, exports JSON, and the Python engine executes it.
