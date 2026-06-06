#!/usr/bin/env bash
# Chat Completions API — the classic OpenAI endpoint.
# No SDK. Just HTTP. JSON in, JSON out.
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1-mini",
    "messages": [
      {"role": "system", "content": "You are a terse assistant."},
      {"role": "user",   "content": "Say hello in one sentence."}
    ],
    "temperature": 0.7
  }'
