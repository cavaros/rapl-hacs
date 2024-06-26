"""Sensor platform for integration_blueprint."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.const import (
    UnitOfPower
)

from .const import DOMAIN
from .coordinator import BlueprintDataUpdateCoordinator
from .entity import IntegrationBlueprintEntity

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="integration_blueprint_2",
        name="Consumo de energia (notebook) (W)",
        icon="mdi:format-quote-close",
    ),
)


async def async_setup_entry(hass, entry, async_add_devices):
    """Set up the sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        IntegrationBlueprintSensor(
            coordinator=coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class IntegrationBlueprintSensor(IntegrationBlueprintEntity, SensorEntity):
    """integration_blueprint Sensor class."""

    def __init__(
        self,
        coordinator: BlueprintDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._attr_native_unit_of_measurement = UnitOfPower.WATT

    @property
    def native_value(self) -> str:
        """Return the native value of the sensor."""
        import subprocess, json
        value = 0
        try:
            teste = json.loads(subprocess.run(['/config/execpowernote.sh'], stdout=subprocess.PIPE).stdout.decode('utf-8'))["powercap"]
            value = teste
            return value if value >= 0 else 0
        except:
            return value if value >= 0 else 0
