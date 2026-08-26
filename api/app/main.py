from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import mock, tasks

app = FastAPI(title="frontend-design-lab API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mock.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")


@app.get("/api/health")
def health():
    return {"status": "ok"}
