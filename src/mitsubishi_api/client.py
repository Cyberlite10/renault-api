"""High-level read-only Mitsubishi connected-car client."""

from collections.abc import Mapping
from typing import Any

from . import const
from .models import MitsubishiResponse
from .session import MitsubishiSession


class MitsubishiClient:
    """Expose only status/history/location operations; no remote commands."""

    def __init__(self, session: MitsubishiSession) -> None:
        self.session = session

    async def _read(
        self, path: str, payload: Mapping[str, Any] | None = None
    ) -> MitsubishiResponse:
        return await self.session.request(path, payload=payload)

    async def get_vehicles(self) -> MitsubishiResponse:
        return await self._read(const.VEHICLE_LIST_PATH)

    async def get_vehicle_status(self, vehicle_id: str) -> MitsubishiResponse:
        return await self._read(const.VEHICLE_STATUS_PATH, {"vehicleId": vehicle_id})

    async def get_charge_details(self, vehicle_id: str) -> MitsubishiResponse:
        return await self._read(const.CHARGE_DETAILS_PATH, {"vehicleId": vehicle_id})

    async def get_charging_history(self, vehicle_id: str) -> MitsubishiResponse:
        return await self._read(const.CHARGING_HISTORY_PATH, {"vehicleId": vehicle_id})

    async def get_mileage_history(self, vehicle_id: str) -> MitsubishiResponse:
        return await self._read(const.MILEAGE_HISTORY_PATH, {"vehicleId": vehicle_id})

    async def get_climate_details(self, vehicle_id: str) -> MitsubishiResponse:
        return await self._read(const.CLIMATE_DETAILS_PATH, {"vehicleId": vehicle_id})

    async def get_charge_schedule(self, vehicle_id: str) -> MitsubishiResponse:
        return await self._read(const.CHARGE_SCHEDULE_PATH, {"vehicleId": vehicle_id})

    async def get_climate_schedule(self, vehicle_id: str) -> MitsubishiResponse:
        return await self._read(const.CLIMATE_SCHEDULE_PATH, {"vehicleId": vehicle_id})

    async def get_vehicle_location(self, vehicle_id: str) -> MitsubishiResponse:
        return await self._read(const.VEHICLE_LOCATION_PATH, {"vehicleId": vehicle_id})

    async def get_available_services(self, vehicle_id: str) -> MitsubishiResponse:
        return await self._read(
            const.AVAILABLE_SERVICES_PATH, {"vehicleId": vehicle_id}
        )
