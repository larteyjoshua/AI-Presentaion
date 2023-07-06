from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
import pickle

models = {}
rate_model_load = Path("app/asset/ai_model/rate_model.pkl")
rate_model_load_2 = Path("app/asset/ai_model/rate_model_rf.pkl")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    with open(rate_model_load, 'rb') as file:
        models['rate_model'] = pickle.load(file)

    with open(rate_model_load_2, 'rb') as file:
        models['rate_model_rf'] = pickle.load(file)

    yield
    # Clean up the ML models and release the resources
    models.clear()
