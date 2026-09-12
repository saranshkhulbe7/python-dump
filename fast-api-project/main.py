from fastapi import FastAPI

app = FastAPI()


def my_decorator(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print("api route hit")
        return result

    return wrapper


@my_decorator
def greet(name):
    print("Hello", name)


@app.get("/")
async def root():
    greet("Saransh")
    return {"message": "Hello World"}
