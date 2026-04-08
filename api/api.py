import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
import json
import fastjsonschema

# Engine imports
from engine.core import run_workflow, validate_workflow
from engine.logging_config import setup_logging

# -----------------------------------
# Initialize logging for the API
# -----------------------------------
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI()

# -----------------------------------
# CORS (React frontend)
# -----------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # replace with your React domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------
# Load JSON Schema
# -----------------------------------
try:
    schema_path = Path("schemas/workflow.schema.json")
    with schema_path.open() as f:
        workflow_schema = json.load(f)

    validate_schema = fastjsonschema.compile(workflow_schema)
    logger.info("Workflow schema loaded successfully")

except Exception as e:
    logger.exception(f"Failed to load workflow schema: {e}")
    raise RuntimeError("API failed to start due to schema load error")

# -----------------------------------
# Request Models
# -----------------------------------
class WorkflowRequest(BaseModel):
    workflow: dict

# -----------------------------------
# Health Check
# -----------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# -----------------------------------
# Validate Workflow (Schema + Engine)
# -----------------------------------
@app.post("/validate")
def validate_endpoint(request: WorkflowRequest):
    try:
        logger.info("Received workflow for validation")

        # 1. JSON Schema validation
        validate_schema(request.workflow)

        # 2. Engine-level validation
        validate_workflow(request.workflow)

        logger.info("Workflow validated successfully")
        return {"status": "valid"}

    except fastjsonschema.JsonSchemaException as e:
        logger.warning(f"Schema validation failed: {e}")
        raise HTTPException(status_code=400, detail=f"Schema validation failed: {str(e)}")

    except Exception as e:
        logger.error(f"Engine validation failed: {e}")
        raise HTTPException(status_code=400, detail=f"Engine validation failed: {str(e)}")

# -----------------------------------
# Run Workflow
# -----------------------------------
@app.post("/run-workflow")
def run_workflow_endpoint(request: WorkflowRequest):
    try:
        logger.info("Received workflow for execution")
        result = run_workflow(request.workflow)
        logger.info("Workflow executed successfully")
        return {"status": "success", "result": result}

    except Exception as e:
        logger.exception(f"Workflow execution failed: {e}")
        raise HTTPException(status_code=500, detail=f"Workflow execution failed: {str(e)}")
