from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
import json
import fastjsonschema

# Import your engine logic
from engine.core import run_workflow, validate_workflow

app = FastAPI()

# -----------------------------
# CORS (React frontend needs this)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # replace with your React domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Load JSON Schema
# -----------------------------
schema_path = Path("schemas/workflow.schema.json")
with schema_path.open() as f:
    workflow_schema = json.load(f)

validate_schema = fastjsonschema.compile(workflow_schema)

# -----------------------------
# Request Models
# -----------------------------
class WorkflowRequest(BaseModel):
    workflow: dict

# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# -----------------------------
# Validate Workflow (Schema + Engine)
# -----------------------------
@app.post("/validate")
def validate_endpoint(request: WorkflowRequest):
    try:
        # 1. Validate against JSON Schema
        validate_schema(request.workflow)

        # 2. Validate using your engine logic
        validate_workflow(request.workflow)

        return {"status": "valid"}

    except fastjsonschema.JsonSchemaException as e:
        raise HTTPException(status_code=400, detail=f"Schema validation failed: {str(e)}")

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Engine validation failed: {str(e)}")

# -----------------------------
# Run Workflow
# -----------------------------
@app.post("/run-workflow")
def run_workflow_endpoint(request: WorkflowRequest):
    try:
        result = run_workflow(request.workflow)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
