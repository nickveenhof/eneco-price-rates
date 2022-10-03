
from typing import NamedTuple
from collections import namedtuple
import logging
from custom_components.eneco_price_rates.types import DayAndNightPrice, DayPrice, ElectricityPrice, NightPrice
import tabula as tb

_LOGGER = logging.getLogger(__name__)


def parse_electricity_price_from_pdf(filename: str) -> ElectricityPrice:
    def to_float(value: str) -> float:
        return float(value.replace(',', '.'))

    data = tb.read_pdf(filename, pages=1)
    yearly_fee = to_float(data[0].iloc[2][0])

    dayPrice = DayPrice(yearly_fee, 
            to_float(data[0].iloc[1][1]) / 100)
    nightPrice = NightPrice(yearly_fee, 
            to_float(data[0].iloc[1][5]) / 100)
    dayAndNightPrice = DayAndNightPrice(yearly_fee, 
        to_float(data[0].iloc[1][2]) / 100, to_float(data[0].iloc[1][3]) / 100)

    return ElectricityPrice(dayPrice, nightPrice, dayAndNightPrice)
