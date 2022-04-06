"""Config flow to configure."""

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_API_KEY
from homeassistant.exceptions import HomeAssistantError
from homeassistant.util.json import load_json
import homeassistant.helpers.config_validation as cv

from .const import ( _LOGGER, DOMAIN, DATA_WU_CONFIG,
                    CONF_PWS_ID, CONF_LANG, DEFAULT_LANG, LANG_CODES)


class WuFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle config flow."""

    VERSION = 1

    def __init__(self):
        """Initialize the flow."""
        self._wu = None

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

        #if user_input is not None:
            # Use the user-supplied API key
            #self._ecobee = Ecobee(config={ECOBEE_API_KEY: user_input[CONF_API_KEY]})

            #if await self.hass.async_add_executor_job(self._ecobee.request_pin):
                # We have a PIN; move to the next step of the flow.
                #return await self.async_step_authorize()
            #errors["base"] = "pin_request_failed"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_API_KEY, default=stored_api_key): str,
                    vol.Required(CONF_PWS_ID): cv.string,
                    vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.All(vol.In(LANG_CODES))
                }
            ),
            errors=errors,
        )

    

    
