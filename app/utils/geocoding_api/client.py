import logging

from app.utils.mapbox_client import MapboxClient

logger = logging.getLogger(__name__)


class GeocodingAPIClient(MapboxClient):
    def __init__(self):
        super().__init__()
        self.api_url = f"{self.api_url}/geocoding/v5/mapbox.places"

    async def get_coordinates(self, address: str) -> dict:
        # url-encode address
        address = address.replace(" ", "%20")
        resp = await self.session_get(
            f"{self.api_url}/{address}.json?access_token={self.api_key}"
        )
        if resp.status != 200:
            logger.error(
                f"Geocoding API returned {resp.status} status code. Error: {resp.reason}"
            )
            return {}
        return await resp.json()
