"""The Volcano integration."""
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .volcanobt.volcano import Volcano

_LOGGER = logging.getLogger(__name__)

DOMAIN = "volcano"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Volcano from a config entry."""
    mac_address = entry.data["mac_address"]
    volcano = Volcano(mac_address)
    await volcano.connect()
    await volcano.initialize_metrics()

    hass.data[DOMAIN] = {
        "volcano": volcano
    }

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "climate")
    )

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(entry, "climate")

    return True
