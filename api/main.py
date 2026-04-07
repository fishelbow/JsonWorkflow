from fastapi import FastAPI
from pydantic import BaseModel
from engine.core import run_workflow  # your engine logic

app = FastAPI()

class WorkflowRequest(BaseModel):
    workflow: dict

@app.post("/run-workflow")
def run_workflow_endpoint(request: WorkflowRequest):
    result = run_workflow(request.workflow)
    return {"status": "success", "result": result}
