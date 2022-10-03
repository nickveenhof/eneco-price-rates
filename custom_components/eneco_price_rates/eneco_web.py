import logging
from typing import NamedTuple
import aiohttp
import asyncio
from bs4 import BeautifulSoup

from custom_components.eneco_price_rates.types import EnecoInfo, EnecoProduct

_LOGGER = logging.getLogger(__name__)

WEBSITE = "https://eneco.be/nl/elektriciteit-gas/tariefkaarten"


class EnecoWeb:
    def __init__(self):
        pass

    async def fetch_page(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(WEBSITE) as response:
                return await response.text()

    async def fetch_electricity_products(self) -> list[EnecoProduct]:
        products: list[EnecoProduct] = []
        soup = BeautifulSoup(await self.fetch_page(), "html.parser")
        for item in soup.select(
            "div.col-lg-7 > div > div:nth-child(1) > div > ul > li > a"
        ):
            products.append(EnecoProduct(item.get_text(), item.get("href")))
        period = (
            soup.select_one(
                "#ewk-app > header > div > div > div > div.header__content > h1"
            )
            .get_text()
            .replace("Tariefkaarten ", "")
        )
        return EnecoInfo(period, products)


if __name__ == "__main__":
    web = EnecoWeb()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(web.fetch_electricity_products())
