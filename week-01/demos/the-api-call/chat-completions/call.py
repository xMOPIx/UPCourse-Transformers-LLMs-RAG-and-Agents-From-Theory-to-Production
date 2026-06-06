"""Chat Completions API — the classic endpoint, via the openai SDK."""
from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY from the environment

resp = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a terse assistant."},
        {"role": "user",   "content": "Say hello in one sentence."},
    ],
    temperature=0.7,
)

print(resp.choices[0].message.content)
print(resp.usage)  # prompt / completion / total tokens
