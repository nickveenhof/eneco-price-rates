from typing import Dict, Optional
from homeassistant import config_entries
from custom_components.eneco_price_rates.const import DOMAIN
from custom_components.eneco_price_rates.eneco_web import EnecoWeb
import homeassistant.helpers.config_validation as cv
import voluptuous as vol


class EnecoPriceRatesConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Eneco Price Rates config flow."""

    data: Optional[str]

    async def async_step_user(self, user_input: Optional[str] = None):
        """Invoked when a user initiates a flow via the user interface."""
        errors: Dict[str, str] = {}
        if user_input is not None:
            errors["base"] = "auth"

        web = EnecoWeb()
        info = await web.fetch_electricity_products()

        options_schema = vol.Schema(
            {
                vol.Optional("Products", default=info.product_names()): cv.multi_select(
                    info.products
                ),
            }
        )
        return self.async_show_form(
            step_id="user", data_schema=options_schema, errors=errors
        )
