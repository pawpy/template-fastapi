import os

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello from FastAPI!"}


@app.get("/health", response_class=PlainTextResponse)
def health():
    return "ok\n"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
