"""Tests for the Eneco PDF module."""
from unittest.mock import AsyncMock, MagicMock
from custom_components.eneco_price_rates.eneco_web import EnecoWeb
from custom_components.eneco_price_rates.eneco_pdf import DayPrice, parse_electricity_price_from_pdf


async def test_parse_electricity_price_from_pdf(hass, aioclient_mock):
    filename = "./tests/data/BC_032_012210_NL_ENECO_POWER_FLEX.pdf"
    result = parse_electricity_price_from_pdf(filename)

    dayAndNightPrice = result.dayAndNightPrice
    assert dayAndNightPrice.yearly_fee == 52.56
    assert dayAndNightPrice.day_price == 0.5244
    assert dayAndNightPrice.night_price == 0.5216

    dayPrice = result.dayPrice
    assert dayPrice.yearly_fee == 52.56
    assert dayPrice.day_price == 0.5229

    nightPrice = result.nightPrice
    assert nightPrice.yearly_fee == 52.56
    assert nightPrice.night_price == 0.5216