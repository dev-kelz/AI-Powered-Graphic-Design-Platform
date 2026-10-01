from app.ai.graph import run_generation


def test_generation_hook_preserves_prompt():
    state = run_generation({"prompt": "editorial poster"})
    assert state["prompt"] == "editorial poster"
