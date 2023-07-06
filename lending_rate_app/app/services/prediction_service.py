from app.models.schemas import ModeLInput
from pathlib import Path
import pandas as pd
from app.services.context_manager import models


async def predict(params: ModeLInput):
    inflations = params.inflation
    eco_growth = params.economic_growth
    inputData = pd.DataFrame(
        {'Inflation(%)': inflations, 'Economic Growth(%)': eco_growth})
    rate_model = models["rate_model"].predict(inputData)
    print(rate_model.tolist())
    return {'result': rate_model.tolist()}


async def predict_rf(params: ModeLInput):
    inflations = params.inflation
    eco_growth = params.economic_growth
    inputData = pd.DataFrame(
        {'Inflation(%)': inflations, 'Economic Growth(%)': eco_growth})
    rate_model = models["rate_model_rf"].predict(inputData)

    return {'result': rate_model.tolist()}
