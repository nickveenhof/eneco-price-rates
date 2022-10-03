
from typing import NamedTuple
from collections import namedtuple
import logging
import tabula as tb

_LOGGER = logging.getLogger(__name__)

class DayAndNightPrice(NamedTuple):
    yearly_fee: float
    day_price: float
    night_price: float

class DayPrice(NamedTuple):
    yearly_fee: float
    day_price: float

class NightPrice(NamedTuple):
    yearly_fee: float
    night_price: float

class ElectricityPrice(NamedTuple):
    dayPrice: DayPrice
    nightPrice: NightPrice
    dayAndNightPrice: DayAndNightPrice


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


if __name__ == '__main__':
    pass