"""Responses API — OpenAI's newer endpoint, via the openai SDK."""
from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY from the environment

resp = client.responses.create(
    model="gpt-4.1-mini",
    instructions="You are a terse assistant.",
    input="Say hello in one sentence.",
)

print(resp.output_text)
print(resp.usage)  # input / output / total tokens
