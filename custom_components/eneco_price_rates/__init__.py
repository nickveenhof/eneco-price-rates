"""Eneco Price Rate Component."""
import logging

from homeassistant import core
from homeassistant.helpers.typing import ConfigType

DOMAIN = "eneco_price_rates"

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: core.HomeAssistant, config: ConfigType) -> bool:
    """Set up the Eneco Price Rates component from yaml configuration."""
    hass.helpers.discovery.load_platform("sensor", DOMAIN, {}, config)

    return True
