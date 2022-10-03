from typing import NamedTuple


class EnecoProduct(NamedTuple):
    name: str
    pdf: str


class EnecoInfo(NamedTuple):
    period: str
    products: list[EnecoProduct]

    def product_names(self) -> list[str]:
        map(lambda x: x.name, self.products)


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
