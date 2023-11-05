import logging
from contextlib import asynccontextmanager

import aiohttp

from app.core.config import settings

logger = logging.getLogger(__name__)


class GeocodingAPIClient:
    def __init__(self):
        self.api_key = settings.GEOCODING_API_KEY
        self.api_url = "https://api.mapbox.com/geocoding/v5/mapbox.places"

    @asynccontextmanager
    async def _create_session(self):
        return aiohttp.ClientSession()

    async def get_coordinates(self, address: str) -> dict:
        # url-encode address
        address = address.replace(" ", "%20")
        async with self._create_session() as session:
            async with session.get(
                    f"{self.api_url}/{address}.json?access_token={self.api_key}"
            ) as response:
                if response.status != 200:
                    logger.error(
                        f"Geocoding API returned {response.status} status code. Error: {response.reason}"
                    )
                    return {}
                data = await response.json()
                return data
