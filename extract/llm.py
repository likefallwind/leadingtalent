"""LLM 客户端包装。

支持两类 provider：
  - anthropic: 原生 Anthropic SDK
  - openai_compat: OpenAI 兼容 API（覆盖 OpenAI / DeepSeek / Qwen / SiliconFlow / 任何兼容方案）

每个客户端有相同接口：
    client.complete(system_prompt, user_prompt, temperature, max_tokens) -> str
"""
from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass
from typing import Optional

log = logging.getLogger(__name__)


@dataclass
class ModelConfig:
    id: str
    provider: str
    model: str
    api_key_env: str
    base_url: str = ""
    enabled: bool = True


class LLMError(Exception):
    pass


class AnthropicClient:
    def __init__(self, mc: ModelConfig):
        from anthropic import Anthropic
        api_key = os.environ.get(mc.api_key_env)
        if not api_key:
            raise LLMError(f"环境变量未设置: {mc.api_key_env}")
        self.client = Anthropic(api_key=api_key)
        self.model = mc.model
        self.id = mc.id

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float,
        max_tokens: int,
        timeout: int = 120,
    ) -> str:
        resp = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
            timeout=timeout,
        )
        # 收集所有 text block
        parts = []
        for block in resp.content:
            if hasattr(block, "text"):
                parts.append(block.text)
        return "".join(parts)


class OpenAICompatClient:
    """OpenAI 兼容协议：OpenAI / DeepSeek / Qwen / SiliconFlow / vLLM 等。"""

    def __init__(self, mc: ModelConfig):
        from openai import OpenAI
        api_key = os.environ.get(mc.api_key_env)
        if not api_key:
            raise LLMError(f"环境变量未设置: {mc.api_key_env}")
        self.client = OpenAI(api_key=api_key, base_url=mc.base_url or None)
        self.model = mc.model
        self.id = mc.id

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float,
        max_tokens: int,
        timeout: int = 120,
    ) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
        )
        return resp.choices[0].message.content or ""


def build_client(mc: ModelConfig):
    if mc.provider == "anthropic":
        return AnthropicClient(mc)
    if mc.provider == "openai_compat":
        return OpenAICompatClient(mc)
    raise LLMError(f"未知 provider: {mc.provider}")


def call_with_retry(
    client,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
    max_tokens: int,
    timeout: int,
    retry_max: int,
    retry_backoff: int,
) -> Optional[str]:
    last_err: Optional[Exception] = None
    for attempt in range(retry_max):
        try:
            return client.complete(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=timeout,
            )
        except Exception as e:
            last_err = e
            backoff = retry_backoff * (2**attempt)
            log.warning(f"  [{client.id}] attempt {attempt+1} failed: {e}; sleep {backoff}s")
            time.sleep(backoff)
    log.error(f"  [{client.id}] 全部重试失败: {last_err}")
    return None
