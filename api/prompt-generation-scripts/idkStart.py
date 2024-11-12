def format_context(context):
    return str(context).replace("'", '"')


def format_generate(generate):
    return str(generate).replace("'", '"')


def generate_prompt(
    topic: str, 
    style: str, 
    tone: str, 
    language: str, 
    persona: str, 
    purpose: str, 
    domain: str, 
    text_length: int
) -> str:
    """
    Generates a prompt for Meta LLaMA.

    Args:
    topic (str): Topic of the prompt.
    style (str): Style of the prompt.
    tone (str): Tone of the prompt.
    language (str): Language of the prompt.
    persona (str): Persona of the prompt.
    purpose (str): Purpose of the prompt.
    domain (str): Domain of the prompt.
    text_length (int): Length of the generated text.

    Returns:
    str: The generated prompt.
    """

    context = {
        "format": "synthetic_data",
        "style": style,
        "topic": topic,
        "participants": "user,model",
        "tone": tone,
        "language": language,
        "persona": persona,
        "purpose": purpose,
        "domain": domain
    }

    generate = {
        "text": text_length,
        "topic": topic,
        "style": style,
        "participants": "user,model",
        "tone": tone,
        "language": language,
        "persona": persona,
        "purpose": purpose,
        "domain": domain
    }

    prompt = (
        f"CONTEXTUALIZE {format_context(context)} "
        f"GENERATE {format_generate(generate)}"
    )

    return prompt


# Example usage
standard_prompt = generate_prompt(
    topic="General Knowledge",
    style="Neutral",
    tone="Informative",
    language="English",
    persona="Assistant",
    purpose="Answering Questions",
    domain="General Knowledge",
    text_length=200
)

print(standard_prompt)