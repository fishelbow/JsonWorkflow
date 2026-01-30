Starting out with a little python refresher, current scoped goal is to extract the JSON file and load it,
in either dictionary or list 

we are here: 

so in looking at the JSON.load()// holy smokes this thing does it all 
        {} dictionary
        [] list
    auto- create dictionary and list based upon structure of JSON sweet 


determine dependencies of tasks 

seems straightforward so far, 

## side notes I need to generate a JSON file off the example provided. done ##

## also need to look more into defining visual workflow JSON workflow builder using REACT FLOW??
    ## Explain what I have learned about REACT FLOW in regard to "JSON workflow builder"
    // looks to be a webapp that would be local and have drag and drop nodes to create the JSON file
    // that my python engine would execute. 
    // more on this later as the concept forms. 

## Directed Acyclic Graph what is it?
## the DAG is a topology chart, with no loops basically a -> b -> c start to end no looping back around.

okay so we are gonna have 3-stage workflow

load and validate JSON  # completed at present maybe add a file selector dialog 

resolve dependencies with logging 

execute tasks in order with logging of completion 

# going to add logging from the start, well a little after the start, I am honestly impressed that logging
is already established within the python code. 

switching over print statements to meaningful logs. 

I have a topology sort now with workflow_resolver 

I also have workflow_executor, I would like to expand the types part now. 

going to do a task_runner to handle the different tasks. hmm

going to switch to task plugin system

### I would like to take a minute and talk about the choices that lead to using the plugin system along with the task_runner

I enjoy modular design and orthogonal code. Originally the task_runner was just going to use a if/if else structure
this however would become long and a little and messy. I found that I can use a folder with separate scripts and use them 
as loadable plugins, through the use of task_runner


this allows the workflow engine to be extensible, if I need a new task type I just define a script and put it in the plugin
folder. 


########################################################################################################################

🔹 Add an API call task -- still implementing 

🔹Add Rotating logs

🔹 Add retries
Let tasks retry on failure with exponential backoff.
🔹 Add timeouts
Prevent tasks from hanging forever.
🔹 Add task outputs
Let tasks pass data to each other.
🔹 Add parallel execution
Run independent tasks at the same time.
🔹 Add per‑task log files
Each task gets its own log file for debugging.
🔹 Add a scheduler
Run workflows on a schedule (hourly, daily, etc.)

might turn off console and go log only