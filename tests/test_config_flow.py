"""Tests for the config flow."""
from unittest import mock
from unittest.mock import AsyncMock, patch

from gidgethub import BadRequest
from homeassistant.const import CONF_ACCESS_TOKEN, CONF_NAME, CONF_PATH
import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.eneco_price_rates import config_flow
from custom_components.eneco_price_rates.const import DOMAIN
from tests.test_eneco_web import HTML_RESPONSE_10_22


@patch("custom_components.eneco_price_rates.config_flow.EnecoWeb")
async def test_flow_user_init(enecoWeb, hass):
    """Test the initialization of the form in the config flow."""
    instance = AsyncMock()
    instance.fetch_page = AsyncMock(return_value=HTML_RESPONSE_10_22)
    enecoWeb.return_value = instance
    result = await hass.config_entries.flow.async_init(
        config_flow.DOMAIN, context={"source": "user"}
    )
    expected = {
        "data_schema": [],
        "description_placeholders": None,
        "errors": {},
        "flow_id": mock.ANY,
        "handler": "eneco_price_rates",
        "last_step": None,
        "step_id": "user",
        "type": "form",
    }
    assert expected["handler"] == result["handler"]
