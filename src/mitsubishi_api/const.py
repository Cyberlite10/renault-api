"""Constants for the Mitsubishi Motors connected-car API."""

DEFAULT_BASE_URL = "https://mitsubishi-prod-mmc.4dcloud.fr/prod"

VEHICLE_LIST_PATH = "/vehicle/getVehicleList/v1"
VEHICLE_STATUS_PATH = "/status/getVSR/v1"
CHARGE_DETAILS_PATH = "/status/getChargeDetails/v1"
CHARGING_HISTORY_PATH = "/status/getChargingHistory/v1"
MILEAGE_HISTORY_PATH = "/status/getMileageHistory/v1"
CLIMATE_DETAILS_PATH = "/status/getClimateDetails/v1"
CHARGE_SCHEDULE_PATH = "/status/getChargeSchedule/v1"
CLIMATE_SCHEDULE_PATH = "/status/getClimateSchedule/v1"
VEHICLE_LOCATION_PATH = "/remote/getVehicleLocation/v1"
AVAILABLE_SERVICES_PATH = "/remote/getAvailableService/v1"
