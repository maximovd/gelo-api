import logging

from fastapi import Depends
from starlette import status
from fastapi import APIRouter, HTTPException

from app.api.gelo.v1.schemas import InferenceIn, InferenceOut
from app.api.common.auth import get_token, Auth
from app.service import llm, enriched_prompt
from app.core.settings import config

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/inference", name="gelo:inference:post", status_code=status.HTTP_200_OK)
async def get_inference(
    inference: InferenceIn,
    _: Auth = Depends(get_token),
) -> InferenceOut:
    prompt = enriched_prompt(inference.prompt)
    try:
        output: dict = llm(prompt, max_tokens=config.LLM.MAX_TOKENS, echo=config.LLM.ECHO)
    except Exception as e: # TODO: Base exception:
        logger.exception(str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    result = output['choices'][0]['text']

    if not result:
        logger.exception("Get error")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Can't get answer from gelo",
        )

    return InferenceOut(result=result)
