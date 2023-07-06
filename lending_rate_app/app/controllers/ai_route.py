from fastapi import APIRouter
from app.services.prediction_service import predict, predict_rf
from app.models.schemas import ModeLInput, ModeLOutput

router = APIRouter(
    prefix='/v1')


@router.post("/predict",  response_model=ModeLOutput)
async def prediction(params: ModeLInput):
    return await predict(params)


@router.post("/predict-rf",  response_model=ModeLOutput)
async def prediction_rf(params: ModeLInput):
    return await predict_rf(params)
