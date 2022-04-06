"""Config flow for Wunderground PWS Intergration."""


import voluptuous as vol
from homeassistant import config_entries, core, exceptions
from homeassistant.core import callback
from .const import _LOGGER, DATA_WU_CONFIG, DOMAIN

class wundergroundCongfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for the Wunderground pws intergration"""
    VERSION = 1
    
    def __init__(self):
        """Initialize the wunderground flow."""
        self._wunderground = None
    
    async def async_step_user(self, user_input=None):
        """Handle a flow initiated by the user."""
        if self._async_current_entries():
            # Config entry already exists, only one allowed.
            return self.async_abort(reason="single_instance_allowed")

        errors = {}
        stored_api_key = (
            self.hass.data[DATA_WU_CONFIG].get(CONF_API_KEY)
            if DATA_WU_CONFIG in self.hass.data
            else ""
        )

        if user_input is not None:
            # Use the user-supplied API key
            self._ecobee = Wunderground(config={WU_API_KEY: user_input[CONF_API_KEY]})

            if await self.hass.async_add_executor_job(self._ecobee.request_pin):
                # We have a PIN; move to the next step of the flow.
                return await self.async_step_authorize()
            errors["base"] = "pin_request_failed"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {vol.Required(CONF_API_KEY, default=stored_api_key): str}
            ),
            errors=errors,
        )

    async def async_step_import(self, device_config):
        """Import a configuration.yaml config, if any."""
        try:
            await validate_input(self.hass, device_config)
        except AlreadyConfigured:
            return self.async_abort(reason="already_configured")

