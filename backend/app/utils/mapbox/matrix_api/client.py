import asyncio
import logging

from app.utils.mapbox.mapbox_client import MapboxClient

logger = logging.getLogger(__name__)


class MatrixAPIClient(MapboxClient):
    def __init__(self):
        super().__init__()
        self.api_url = f"{self.api_url}/directions-matrix/v1"

    async def get_matrix(self, coordinates: list) -> dict:
        # url-encode address
        coordinates = ";".join(
            [",".join([str(c) for c in coord]) for coord in coordinates]
        )
        resp = await self.session_get(
            f"{self.api_url}/mapbox/driving/{coordinates}?access_token={self.api_key}"
        )
        return await resp.json()
