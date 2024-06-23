# /api/v1/gelo/inference


from pydantic import BaseModel, Field


class InferenceIn(BaseModel):
    prompt: str = Field(..., description="Запрос к модели.")


class InferenceOut(BaseModel):
    result: str
    # TODO: Подумать, какие еще данные на выход лучше отдавать