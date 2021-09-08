from httpx import AsyncClient

import pytest

from main import app


@pytest.mark.asyncio
async def test_team_list():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/teams/")
    assert response.status_code == 200
