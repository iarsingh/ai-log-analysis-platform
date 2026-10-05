from ailogs.ops import router as ops_router
from fastapi import FastAPI, HTTPException
from ailogs.classify import InputError, classify

app = FastAPI()
app.include_router(ops_router, prefix="/v1")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/classify")
def post_classify(body: dict):
    try:
        return classify(body.get("text", ""))
    except InputError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
