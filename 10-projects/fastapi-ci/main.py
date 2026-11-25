from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Hello devops"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test")
def test():
    return{"test" : "ok"}    