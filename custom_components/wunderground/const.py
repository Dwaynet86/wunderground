"""Constants for the wunderground pws integration."""

import logging

from homeassistant.components.weather import (
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_HAIL,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_SUNNY,
    ATTR_CONDITION_WINDY,
)
from homeassistant.const import Platform

_LOGGER = logging.getLogger(__package__)

DOMAIN = "wunderground"
DATA_WU_CONFIG = "wunderground_config"

CONF_INDEX = "index"
CONF_REFRESH_TOKEN = "refresh_token"

PLATFORMS = [
    Platform.BINARY_SENSOR,
    Platform.CLIMATE,
    Platform.HUMIDIFIER,
    Platform.SENSOR,
    Platform.WEATHER,
]
