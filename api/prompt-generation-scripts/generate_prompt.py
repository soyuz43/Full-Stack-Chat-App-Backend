def generate_prompt(
    topic: str,
    style: str,
    tone: str,
    language: str,
    persona: str,
    purpose: str,
    domain: str,
    text_length: int,
) -> str:
    """
    Generates a prompt for Meta LLaMA 3.

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
        "domain": domain,
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
        "domain": domain,
    }

    prompt = (
        f"""CONTEXTUALIZE {str(context).replace("'", '"')} """
        f"""GENERATE {str(generate).replace("'", '"')}"""
    )


    return prompt.strip()  # Remove leading/trailing spaces


# Example usage
prompt = generate_prompt(
    topic="LLaMA 3 command syntax",
    style="Official documentation",
    tone="Informative",
    language="English",
    persona="Meta LLaMA 3",
    purpose="Mastering of the LLaMA 3 Command Syntax",
    domain="SYNTAXDOCS",
    text_length=400,
)

print(prompt)