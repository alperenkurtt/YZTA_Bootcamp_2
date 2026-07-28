from openai import OpenAI

from config import OPENROUTER_API_KEY

MODEL = "openai/gpt-4o-mini"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)


def get_response(messages: list[dict]) -> str:
    completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    return completion.choices[0].message.content
