from fastapi import FastAPI, HTTPException
from App.service import prever
from App.schemas import PredictRequest, PredictResponse


app = FastAPI(
    title="Credix API",
    version="1.0.0"
)

@app.post(
    "/predict",
    response_model=PredictResponse
)
def predict(
    request: PredictRequest
):

    resposta = prever(request)

    if resposta is None:

        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    return resposta