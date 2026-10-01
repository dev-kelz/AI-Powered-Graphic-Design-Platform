from pathlib import Path

ALLOWED_IMAGE_TYPES = {"image/png", "image/jpeg", "image/webp"}


def is_allowed_image(filename: str, content_type: str | None) -> bool:
    return Path(filename).suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"} and content_type in ALLOWED_IMAGE_TYPES
