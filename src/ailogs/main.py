from fastapi import FastAPI, HTTPException
from ailogs.classify import InputError, classify

app = FastAPI()


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/classify")
def post_classify(body: dict):
    try:
        return classify(body.get("text", ""))
    except InputError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
