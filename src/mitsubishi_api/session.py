"""Authenticated, read-only HTTP transport for Mitsubishi Motors."""

from collections.abc import Mapping
from typing import Any

import aiohttp

from .const import DEFAULT_BASE_URL
from .exceptions import MitsubishiApiError
from .exceptions import MitsubishiAuthenticationError
from .models import MitsubishiResponse


class MitsubishiSession:
    """Make authenticated GET/POST requests to an allowlist of read endpoints."""

    def __init__(
        self,
        websession: aiohttp.ClientSession,
        access_token: str,
        *,
        base_url: str = DEFAULT_BASE_URL,
        token_header: str = "knt-access-token",
        extra_headers: Mapping[str, str] | None = None,
    ) -> None:
        if not access_token:
            raise ValueError("access_token must not be empty")
        self._websession = websession
        self._base_url = base_url.rstrip("/")
        self._headers = {
            "Accept": "application/json",
            token_header: access_token,
            **dict(extra_headers or {}),
        }

    async def request(
        self,
        path: str,
        *,
        method: str = "POST",
        payload: Mapping[str, Any] | None = None,
    ) -> MitsubishiResponse:
        """Request a read-only endpoint and return its vendor JSON unchanged."""
        async with self._websession.request(
            method,
            f"{self._base_url}{path}",
            headers=self._headers,
            json=dict(payload or {}),
        ) as response:
            if response.status in (401, 403):
                raise MitsubishiAuthenticationError(
                    f"Mitsubishi authentication failed ({response.status})"
                )
            if response.status >= 400:
                body = await response.text()
                raise MitsubishiApiError(
                    f"Mitsubishi API request failed ({response.status}): {body[:200]}"
                )
            data = await response.json()
            if not isinstance(data, (dict, list)):
                raise MitsubishiApiError("Mitsubishi API returned non-object JSON")
            return MitsubishiResponse(status=response.status, data=data)
