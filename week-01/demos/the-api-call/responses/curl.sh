#!/usr/bin/env bash
# Responses API — OpenAI's newer endpoint (2025+).
# Same idea, simpler surface: one `input`, one `output_text`.
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1-mini",
    "instructions": "You are a terse assistant.",
    "input": "Say hello in one sentence."
  }'
