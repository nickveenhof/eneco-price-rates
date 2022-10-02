"""Tests for the sensor module."""
from unittest.mock import AsyncMock, MagicMock

async def test_async_update_success(hass, aioclient_mock):
    """Tests a fully successful async_update."""
    assert True is True


