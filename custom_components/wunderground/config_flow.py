"""Config flow for Wunderground PWS Intergration."""


import voluptuous as vol
from homeassistant import config_entries, core, exceptions
from homeassistant.core import callback
from .const import _LOGGER, DATA_WU_CONFIG, DOMAIN

class wuCongfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
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
        stored_pws_id = (
            self.hass.data[DATA_WU_CONFIG].get(CONF_PWS_ID)
            if DATA_WU_CONFIG in self.hass.data
            else ""
        )

        if user_input is not None:
            # Use the user-supplied API key
            self._wunderground = Wunderground(config={WU_API_KEY: user_input[CONF_API_KEY]})
            self._wunderground = Wunderground(config={WU_PWS_ID: user_input[CONF_PWS_ID]})
            
            errors["base"] = "failed"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {vol.Required(CONF_API_KEY, default=stored_api_key): str},
                {vol.Required(CONF_PWS_ID, default=stored_pws_id): str}
            ),
            errors=errors,
        )
        config = {
           CONF_API_KEY: self._wunderground.api_key,
           CONF_PWS_ID: self._wunderground.pws_id,
                }
        return self.async_create_entry(title=DOMAIN, data=config)
    

