"""Volcano climate platform."""
from homeassistant.components.climate import (
    ClimateEntity,
    SUPPORT_TARGET_TEMPERATURE,
)
from homeassistant.const import ATTR_TEMPERATURE, TEMP_CELSIUS

from . import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Volcano climate platform."""
    volcano = hass.data[DOMAIN]["volcano"]
    async_add_entities([VolcanoClimate(volcano)])

class VolcanoClimate(ClimateEntity):
    """Representation of the Volcano climate entity."""

    def __init__(self, volcano):
        """Initialize the Volcano climate entity."""
        self._volcano = volcano

    @property
    def name(self):
        """Return the name of the climate entity."""
        return "Volcano"

    @property
    def temperature_unit(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    @property
    def current_temperature(self):
        """Return the current temperature."""
        return self._volcano.temperature

    @property
    def target_temperature(self):
        """Return the target temperature."""
        return self._volcano.target_temperature

    async def async_set_temperature(self, **kwargs):
        """Set target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature is not None:
            await self._volcano.set_target_temperature(temperature)

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return SUPPORT_TARGET_TEMPERATURE