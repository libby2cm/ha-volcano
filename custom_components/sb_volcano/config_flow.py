"""Config flow for Volcano integration."""
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_MAC

from .const import DOMAIN

class VolcanoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Volcano."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            mac_address = user_input[CONF_MAC]
            # TODO: Add validation for the MAC address (e.g., check format, uniqueness, connectivity)
            return self.async_create_entry(
                title=mac_address,
                data={CONF_MAC: mac_address},
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required(CONF_MAC): str}),
            errors=errors,
        )
