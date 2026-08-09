"""Tests for the read-only Mitsubishi API client."""

from unittest.mock import Mock

import aiohttp
import pytest

from mitsubishi_api import MitsubishiAuthenticationError
from mitsubishi_api import MitsubishiClient
from mitsubishi_api import MitsubishiSession


class FakeResponse:
    def __init__(self, status: int, data: object) -> None:
        self.status = status
        self._data = data

    async def __aenter__(self) -> "FakeResponse":
        return self

    async def __aexit__(self, *args: object) -> None:
        return None

    async def json(self) -> object:
        return self._data

    async def text(self) -> str:
        return str(self._data)


@pytest.mark.asyncio
async def test_vehicle_status_uses_read_endpoint() -> None:
    websession = Mock(spec=aiohttp.ClientSession)
    websession.request.return_value = FakeResponse(200, {"battery": {"soc": 80}})
    client = MitsubishiClient(MitsubishiSession(websession, "test-token"))

    result = await client.get_vehicle_status("vehicle-1")

    assert result.data == {"battery": {"soc": 80}}
    websession.request.assert_called_once_with(
        "POST",
        "https://mitsubishi-prod-mmc.4dcloud.fr/prod/status/getVSR/v1",
        headers={"Accept": "application/json", "knt-access-token": "test-token"},
        json={"vehicleId": "vehicle-1"},
    )


@pytest.mark.asyncio
async def test_authentication_error_does_not_expose_token() -> None:
    websession = Mock(spec=aiohttp.ClientSession)
    websession.request.return_value = FakeResponse(401, {"error": "unauthorized"})
    client = MitsubishiClient(MitsubishiSession(websession, "secret-token"))

    with pytest.raises(MitsubishiAuthenticationError) as exc:
        await client.get_vehicles()

    assert "secret-token" not in str(exc.value)
