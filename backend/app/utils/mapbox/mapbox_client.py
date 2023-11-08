from contextlib import asynccontextmanager

import aiohttp

from app.core.config import settings


class MapboxClient:
    def __init__(self):
        self.api_key = settings.MAPBOX_API_KEY
        self.api_url = "https://api.mapbox.com"

    @asynccontextmanager
    async def _create_session(self):
        return aiohttp.ClientSession()

    async def session_get(self, url):
        async with self._create_session() as session:
            async with session.get(url) as response:
                return response
