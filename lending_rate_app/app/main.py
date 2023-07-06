from fastapi import FastAPI
from app.services.context_manager import lifespan
from app.controllers import ai_route
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title='Lending Rate ML Application', lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(ai_route.router)
