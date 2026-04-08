Project Architecture Overview -- Engine orchestration refactor 

-- prior to the API layer, I was using main as the cli and entry point of the porgram.

the project is evolving into 

- Engine layer (workflow logic)

- Cli layer (Local execution)

- API layer (FastAPI service)

- Plugin layer (extensible task types)

this is all in preperation of moving to a container for hosting.

app.py is now the CLI local testing entry point. 

~ loading workflows from disk
~ running them through the engine
~ printing logs and results in the console
~ providing a sandbox for testing the engine locally
~ this seperate the api layer and keep the engine stable
~ for testing. 

$ the abstraction provides stability in the layers 

main.py now Starts the FastAPI server, exposes endpoints and
serves as an entry point for deployment.


right now I have a script for FastAPI i will be spliting it up
as advised by an LLM 

api/
    server.py     # creates FastAPI() instance
    routes.py     # all API endpoints
    models.py     # Pydantic request/response models
    depndencies.py 

# matches FastAPI project structure 

- server.py 
    Creates the FastAPI app and includes routers

- routes.py
    defines endpoints like /run-worklow, /validate, /plugins

- models.py
    defines request/response schemas

- dependecies.py
    Holds shared dependencies 





                      FastAPI Layer
                            |
                            |
                         core.py  # Orchestrator of engine for FastAPI and CLI
                            |
                            |
        ---------------------------------------------------------------------
        |                   |                         |                     |

workflow_loader     workflow_resolver.py      workflow_executor.py      task_runner + plugins 


# As the project evolved, the responsibilities of core.py became clearer. Orginally, core.py was a catch-all file that mixed engine logic, workflow execution, and sometimes even api-related concerns. After restructuring the project, core.py now serves a single, well-defined purpose of orchestrating the engine for the api.

also of note in the moment of realizing that I have 2 orchestrators when
I intend to only have one. 

okay updated app.py 
    - reads workflow JSON from disk
    - calls run_workflow()
    - logs results 
    removed direct ocestration only concern is reading from disk 
    for testing out the engine locally. it now calls the orchestrator 
    passing in the JSON from disk. just going to double check the 
    api layer and make sure its not partaking in any orchestration 


api layer is still just one script atm will update tomorrow

added in logging and added try/catch to schema loading, validation and execution 

next steps will be spliting api.py into (server.py, routes.py, models.py)