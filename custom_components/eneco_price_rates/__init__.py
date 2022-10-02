"""Eneco Price Rate Component."""
import asyncio
import logging

from homeassistant import core

DOMAIN = "eneco_price_rates"

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Eneco Price Rates component from yaml configuration."""
    hass.data.setdefault(DOMAIN, {})
    return True
