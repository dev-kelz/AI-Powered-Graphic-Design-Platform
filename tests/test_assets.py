from app.utils.validators import is_allowed_image


def test_image_validation():
    assert is_allowed_image("poster.png", "image/png")
    assert not is_allowed_image("poster.exe", "application/octet-stream")
