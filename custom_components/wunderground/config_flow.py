"""Config flow for Wunderground PWS Intergration."""


import voluptuous as vol
from homeassistant import config_entries, core, exceptions
from homeassistant.core import callback
from .const import _LOGGER, DATA_WU_CONFIG, DOMAIN, CONF_PWS_ID
from homeassistant.const import CONF_API_KEY
from typing import Any, Dict, Optional
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity_registry import (
    async_entries_for_config_entry,
    async_get_registry,
)

AUTH_SCHEMA = vol.Schema(
    {vol.Required(CONF_API_KEY): cv.string, vol.Required(CONF_PWS_ID): cv.string}
)

class wuConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for the Wunderground pws intergration"""
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH
    def __init__(self):
        """Initialize the wunderground flow."""
        self._wunderground = None
    
    data: Optional[Dict[str, Any]]
    
    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None):
        """Handle a flow initiated by the user."""
        errors: Dict[str, str] = {}
        if user_input is not None:
            #try:
                #await validate_auth(user_input[CONF_ACCESS_TOKEN], self.hass)
            #except ValueError:
                #errors["base"] = "auth"   
             if not errors:
                # Input is valid, set data.
                self.data = user_input
                return self.async_create_entry(title="WUnderground PWS", data=self.data)

        return self.async_show_form(
            step_id="user", data_schema=AUTH_SCHEMA, errors=errors
        )           

        
