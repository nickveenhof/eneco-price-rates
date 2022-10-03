"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    add_entities(
        [
            ElectricityPriceSensor("Energiekost Dagtarief", 0.2627),
            ElectricityPriceSensor("Energiekost Nachttarief", 0.2598),
            GasPriceSensor("Energiekost gasprijs", 0.1122),
        ]
    )


class EnergyPriceSensor(SensorEntity):
    """Representation of an energy price sensor."""

    def __init__(self, name: str, value: float) -> None:
        """Initialize the sensor."""
        super().__init__()
        self._name = name
        self._state = value

    @property
    def unique_id(self) -> str:
        """Return the unique id of the sensor."""
        return self._name.lower().replace(" ", "_")

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement."""
        return "€/kWh"

    async def async_update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        pass


class ElectricityPriceSensor(EnergyPriceSensor):
    """Representation of an electricity price sensor."""

    def __init__(self, name: str, value: float) -> None:
        """Initialize the sensor."""
        super().__init__(name, value)

    @property
    def icon(self) -> str:
        """Return the icon of the sensor."""
        return "mdi:lightning-bolt"


class GasPriceSensor(EnergyPriceSensor):
    """Representation of an gas price sensor."""

    def __init__(self, name: str, value: float) -> None:
        """Initialize the sensor."""
        super().__init__(name, value)

    @property
    def icon(self) -> str:
        """Return the icon of the sensor."""
        return "mdi:barrel"
