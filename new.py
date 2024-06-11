from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def d():
    return{"heloo"}