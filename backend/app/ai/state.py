from typing import TypedDict


class GenerationState(TypedDict, total=False):
    prompt: str
    asset_id: int
    image_url: str
