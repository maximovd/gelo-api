from starlette import status
from fastapi import APIRouter

from app.api.gelo.v1.schemas import InferenceIn, InferenceOut


router = APIRouter()


@router.post("/inference", name="gelo:inference:post", status_code=status.HTTP_200_OK)
async def get_inference(inference: InferenceIn) -> InferenceOut:
    return InferenceOut(result="tests")
