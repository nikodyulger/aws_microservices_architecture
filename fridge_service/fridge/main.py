from fastapi import FastAPI, APIRouter

from fridge.schemas import Product

fridge = FastAPI(title="Fridge API")

fridge_router = APIRouter()

@fridge_router.get('/')
def open_fridge():
    return "Hi! You opened the fridge!"

fridge.include(fridge_router)

if __name__ == "__main__":
    # DEBUGGING
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")