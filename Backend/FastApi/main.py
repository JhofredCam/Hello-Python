from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "hola mundo"

@app.get("/github")
async def url():
    return { "url" : "https://github.com/JhofredCam"}