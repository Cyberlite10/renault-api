# Experimental Mitsubishi connected-car client

This branch contains an experimental, async, **read-only** client for the
Mitsubishi Motors service used by the current mobile application.

The implementation intentionally excludes wake-up, charging, climate, horn,
lights, and lock commands. It currently accepts an existing access token so the
observed read endpoints can be validated before implementing authentication.

## Observed base URL

`https://mitsubishi-prod-mmc.4dcloud.fr/prod`

## Implemented reads

- vehicle list and vehicle status
- charge details and charging history
- mileage history
- climate details
- charge and climate schedules
- vehicle location
- available services

The exact request field names and token lifecycle still require validation
against a redacted capture from an authenticated app session. Do not commit
credentials, tokens, VINs, precise locations, APKs, or unredacted responses.

## Example

```python
import aiohttp

from mitsubishi_api import MitsubishiClient, MitsubishiSession

async with aiohttp.ClientSession() as http:
    session = MitsubishiSession(http, access_token="short-lived token")
    client = MitsubishiClient(session)
    vehicles = await client.get_vehicles()
```
