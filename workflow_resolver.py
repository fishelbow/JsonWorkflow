import logging
from collections import defaultdict, deque

def resolve_dependencies(tasks):

    # tasks: list of task dictionaries from your JSON
    # Returns: list of task IDs in valid execution order
   

    logging.info("Resolving task dependencies")

    graph = defaultdict(list)
    in_degree = defaultdict(int)
    task_ids = set()

    # Initialize nodes
    for task in tasks:
        tid = task["id"]
        task_ids.add(tid)
        in_degree[tid] = 0

    # Build edges
    for task in tasks:
        tid = task["id"]
        deps = task.get("depends_on", [])

        for dep in deps:
            graph[dep].append(tid)
            in_degree[tid] += 1

    # Queue of tasks with no dependencies
    queue = deque([tid for tid in task_ids if in_degree[tid] == 0])

    execution_order = []

    while queue:
        current = queue.popleft()
        execution_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Detect cycles
    if len(execution_order) != len(task_ids):
        logging.error("Cycle detected in workflow dependencies")
        raise ValueError("Cycle detected in workflow dependencies")

    logging.info(f"Dependency resolution complete. Order: {execution_order}")
    return execution_order