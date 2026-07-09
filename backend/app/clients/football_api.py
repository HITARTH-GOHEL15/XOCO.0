from fastapi import FastAPI

app = FastAPI(title="XOCO.0")


@app.get("/")
def health():
    return {"status": "XOCO.0 is running"}
