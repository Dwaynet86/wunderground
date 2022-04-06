"""Config flow for Wunderground PWS Intergration."""
import logging

import voluptuous as vol
from homeassistant import config_entries, core, exceptions
from homeassistant.core import callback

_LOGGER = logging.getLogger(__name__)

from .const import DOMAIN

class wundergroundCongfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for the Wunderground pws intergration"""
    
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_UNKNOWN
    
    async def async_step_import(self, device_config):
        """Import a configuration.yaml config, if any."""
        try:
            await validate_input(self.hass, device_config)
        except AlreadyConfigured:
            return self.async_abort(reason="already_configured")

        wunderground = Wunderground(config=config)
        CONF_API_KEY: wunderground.api_key
        CONF_PWS_ID: wunderground.pws_id
        CONF_NUMERIC_PRECISION: wunderground.numeric_precision
        monitored_conditions
        
        return self.async_create_entry(
            title=f"Ecowitt on port {port}",
            data=device_config
        )
