from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Amadeu Beraldin Portfolio")


@app.get("/health")
def health():
    return JSONResponse({"status": "ok"})
