from typing import Final

from llama_cpp import Llama

from app.core.settings import config


llm = Llama.from_pretrained(
    repo_id=config.LLM.REPO,
    filename=config.LLM.FILENAME,
    verbose=False,
)


def enriched_prompt(prompt: str) -> str:
    result_prompt = f"""[INST]
    {prompt}
    [/INST]
    """
    return result_prompt
