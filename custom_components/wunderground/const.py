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
_RESOURCECURRENT = 'https://api.weather.com/v2/pws/observations/current?stationId={}&format=json&units={}&apiKey={}'
_RESOURCEFORECAST = 'https://api.weather.com/v3/wx/forecast/daily/5day?geocode={},{}&units={}&{}&format=json&apiKey={}'


CONF_ATTRIBUTION = "Data provided by the WUnderground weather s
CONF_LANG = "lang"
CONF_NUMERIC_PRECISION = 'numeric_precision'
CONF_PWS_ID = "pws_id"
DATA_WU_CONFIG = "wunderground_config"
DEFAULT_LANG = 'en-US'
DOMAIN = "wunderground"

PLATFORMS = [
    Platform.BINARY_SENSOR,
    Platform.CLIMATE,
    Platform.HUMIDIFIER,
    Platform.SENSOR,
    Platform.WEATHER,
]

# Language Supported Codes
LANG_CODES = [
    'ar-AE', 'az-AZ', 'bg-BG', 'bn-BD', 'bn-IN', 'bs-BA', 'ca-ES', 'cs-CZ', 'da-DK', 'de-DE', 'el-GR', 'en-GB', 'en-IN',
    'en-US', 'es-AR', 'es-ES', 'es-LA', 'es-MX', 'es-UN', 'es-US', 'et-EE', 'fa-IR', 'fi-FI', 'fr-CA', 'fr-FR', 'gu-IN',
    'he-IL', 'hi-IN', 'hr-HR', 'hu-HU', 'in-ID', 'is-IS', 'it-IT', 'iw-IL', 'ja-JP', 'jv-ID', 'ka-GE', 'kk-KZ', 'kn-IN',
    'ko-KR', 'lt-LT', 'lv-LV', 'mk-MK', 'mn-MN', 'ms-MY', 'nl-NL', 'no-NO', 'pl-PL', 'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU',
    'si-LK', 'sk-SK', 'sl-SI', 'sq-AL', 'sr-BA', 'sr-ME', 'sr-RS', 'sv-SE', 'sw-KE', 'ta-IN', 'ta-LK', 'te-IN', 'tg-TJ',
    'th-TH', 'tk-TM', 'tl-PH', 'tr-TR', 'uk-UA', 'ur-PK', 'uz-UZ', 'vi-VN', 'zh-CN', 'zh-HK', 'zh-TW'
]
