from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def say_something(name: str, message: str):
    return {f"Hello {name}! {message}!"}
