from fastapi import FastAPI



import json
import fastjsonschema
from pathlib import Path

# Load JSON Schema
schema_path = Path("schemas/workflow.schema.json")
with schema_path.open() as f:
    workflow_schema = json.load(f)

validate_schema = fastjsonschema.compile(workflow_schema)
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# test to check the server 