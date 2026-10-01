from app.ai.state import GenerationState


def build_generation_graph():
    """Provider-neutral hook for a future LangGraph workflow."""
    return None


def run_generation(state: GenerationState) -> GenerationState:
    return state
