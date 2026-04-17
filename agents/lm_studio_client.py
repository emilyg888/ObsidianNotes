"""Thin LM Studio chat-completions client for Qwen 2.5-14B.

Mirrors the pattern used by Notes/chunk_aip_c01.py and Notes/query_engine.py so
the same LM_STUDIO_URL / LM_STUDIO_MODEL env vars work here too.
"""
from __future__ import annotations

import json
import os
import re
from typing import Any
from urllib import error, request


LM_STUDIO_URL = os.getenv(
    "LM_STUDIO_URL", "http://127.0.0.1:1234/v1/chat/completions"
)
MODEL_NAME = os.getenv("LM_STUDIO_MODEL", "qwen2.5-14b-instruct")


class LMStudioClient:
    def __init__(
        self,
        url: str = LM_STUDIO_URL,
        model: str = MODEL_NAME,
        default_temperature: float = 0.2,
    ) -> None:
        self.url = url
        self.model = model
        self.default_temperature = default_temperature

    def chat(
        self,
        system: str,
        user: str,
        *,
        temperature: float | None = None,
        max_tokens: int | None = None,
    ) -> str:
        body: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "stream": False,
            "temperature": (
                temperature if temperature is not None else self.default_temperature
            ),
        }
        if max_tokens is not None:
            body["max_tokens"] = max_tokens

        payload = json.dumps(body).encode("utf-8")
        req = request.Request(
            self.url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with request.urlopen(req, timeout=120) as response:
                data = json.loads(response.read().decode("utf-8"))
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(
                f"LM Studio returned HTTP {exc.code}: {detail}"
            ) from exc
        except error.URLError as exc:
            raise RuntimeError(
                "Could not reach LM Studio. Ensure the local server is running "
                f"at {self.url}."
            ) from exc

        choices = data.get("choices", [])
        if not choices:
            return ""
        content = choices[0].get("message", {}).get("content", "")
        if isinstance(content, list):
            parts = [
                item.get("text", "")
                for item in content
                if isinstance(item, dict) and item.get("type") == "text"
            ]
            return "\n".join(parts).strip()
        return str(content).strip()


def parse_json_object(content: str) -> dict[str, Any] | None:
    """Extract a JSON object from a model response, stripping fences if needed."""
    if not content:
        return None
    text = content.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)

    candidates = [text]
    left = text.find("{")
    right = text.rfind("}")
    if left != -1 and right != -1 and right > left:
        candidates.append(text[left : right + 1])

    for candidate in candidates:
        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return parsed
    return None
