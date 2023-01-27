from fastapi import FastAPI

fridge = FastAPI()

@fridge.get('/')
def open_fridge():
    return "Hi! You opened the fridge!"