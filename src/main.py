# this is the start of the program to "turn on" fast api effectivly making the engine live and awaiting a JSON from 
# the react app.

import uvicorn

if __name__ == "__main__":
    uvicorn.run("api.server:app", host="0.0.0.0", port=8000, reload=True)
