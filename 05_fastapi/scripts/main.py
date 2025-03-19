from fastapi import FastAPI, Header
 
app = FastAPI()
 

@app.get("/")
def root(secret_code: str | None = Header(default=None)):
    return {"Secret-Code": secret_code}