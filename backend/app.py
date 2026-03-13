from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Portfolio Homepage API")


@app.get("/health")
def health():
    return JSONResponse({"status": "ok"})
