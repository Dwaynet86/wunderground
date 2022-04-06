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


CONF_ATTRIBUTION = "Data provided by the WUnderground weather service"
CONF_LANG = "lang"
CONF_NUMERIC_PRECISION = 'numeric_precision'
CONF_PWS_ID = "pws_id"
DATA_WU_CONFIG = "wunderground_config"
DEFAULT_LANG = 'en-US'
DOMAIN = "wunderground"

PLATFORMS = [
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

SENSOR_TYPES = {
    # current
    'neighborhood': WUSensorConfig(
        'Neighborhood', 'observations',
        value=lambda wu: wu.data['observations'][0]['neighborhood'],
        icon="mdi:map-marker"),
    'obsTimeLocal': WUSensorConfig(
        'Local Observation Time', 'observations',
        value=lambda wu: wu.data['observations'][0]['obsTimeLocal'],
        icon="mdi:clock"),
    'humidity': WUSensorConfig(
        'Relative Humidity', 'observations',
        value=lambda wu: int(wu.data['observations'][0]['humidity'] or 0),
        unit_of_measurement='%',
        icon="mdi:water-percent",
        device_class="humidity"),
    'stationID': WUSensorConfig(
        'Station ID', 'observations',
        value=lambda wu: wu.data['observations'][0]['stationID'],
        icon="mdi:home"),
    'solarRadiation': WUSensorConfig(
        'Solar Radiation', 'observations',
        value=lambda wu: str(wu.data['observations'][0]['solarRadiation']),
        unit_of_measurement='w/m2',
        icon="mdi:weather-sunny"),
    'uv': WUSensorConfig(
        'UV', 'observations',
        value=lambda wu: str(wu.data['observations'][0]['uv']),
        unit_of_measurement='',
        icon="mdi:sunglasses", ),
    'winddir': WUSensorConfig(
        'Wind Direction', 'observations',
        value=lambda wu: int(wu.data['observations'][0]['winddir'] or 0),
        unit_of_measurement='\u00b0',
        icon="mdi:weather-windy"),
    'today_summary': WUSensorConfig(
        'Today Summary', 'observations',
        value=lambda wu: str(wu.data['narrative'][0]),
        unit_of_measurement='',
        icon="mdi:gauge"),
    # current conditions
    'elev': WUCurrentConditionsSensorConfig(
        'Elevation', 'elev', 'mdi:elevation-rise', ALTITUDEUNIT),
    'dewpt': WUCurrentConditionsSensorConfig(
        'Dewpoint', 'dewpt', 'mdi:water', TEMPUNIT),
    'heatIndex': WUCurrentConditionsSensorConfig(
        'Heat index', 'heatIndex', "mdi:thermometer", TEMPUNIT),
    'windChill': WUCurrentConditionsSensorConfig(
        'Wind chill', 'windChill', "mdi:thermometer", TEMPUNIT),
    'precipRate': WUCurrentConditionsSensorConfig(
        'Precipitation Rate', 'precipRate', "mdi:umbrella", RATE),
    'precipTotal': WUCurrentConditionsSensorConfig(
        'Precipitation Today', 'precipTotal', "mdi:umbrella", LENGTHUNIT),
    'pressure': WUCurrentConditionsSensorConfig(
        'Pressure', 'pressure', "mdi:gauge", PRESSUREUNIT,
        device_class="pressure"),
    'temp': WUCurrentConditionsSensorConfig(
        'Temperature', 'temp', "mdi:thermometer", TEMPUNIT,
        device_class="temperature"),
    'windGust': WUCurrentConditionsSensorConfig(
        'Wind Gust', 'windGust', "mdi:weather-windy", SPEEDUNIT),
    'windSpeed': WUCurrentConditionsSensorConfig(
        'Wind Speed', 'windSpeed', "mdi:weather-windy", SPEEDUNIT),
    # forecast
    'weather_1d': WUDailyTextForecastSensorConfig(0),
    'weather_1n': WUDailyTextForecastSensorConfig(1),
    'weather_2d': WUDailyTextForecastSensorConfig(2),
    'weather_2n': WUDailyTextForecastSensorConfig(3),
    'weather_3d': WUDailyTextForecastSensorConfig(4),
    'weather_3n': WUDailyTextForecastSensorConfig(5),
    'weather_4d': WUDailyTextForecastSensorConfig(6),
    'weather_4n': WUDailyTextForecastSensorConfig(7),
    'weather_5d': WUDailyTextForecastSensorConfig(8),
    'weather_5n': WUDailyTextForecastSensorConfig(9),
    'temp_high_1d': WUDailySimpleForecastSensorConfig(
        "High Temperature Today", 0, "temperature", TEMPUNIT,
        "mdi:thermometer", device_class="temperature"),
    'temp_high_2d': WUDailySimpleForecastSensorConfig(
        "High Temperature Tomorrow", 2, "temperature", TEMPUNIT,
        "mdi:thermometer", device_class="temperature"),
    'temp_high_3d': WUDailySimpleForecastSensorConfig(
        "High Temperature in 3 Days", 4, "temperature", TEMPUNIT,
        "mdi:thermometer", device_class="temperature"),
    'temp_high_4d': WUDailySimpleForecastSensorConfig(
        "High Temperature in 4 Days", 6, "temperature", TEMPUNIT,
        "mdi:thermometer", device_class="temperature"),
    'temp_high_5d': WUDailySimpleForecastSensorConfig(
        "High Temperature in 5 Days", 8, "temperature", TEMPUNIT,
        "mdi:thermometer", device_class="temperature"),
    'temp_low_1d': WUDailySimpleForecastSensorConfig(
        "Low Temperature Today", 1, "temperature", TEMPUNIT,
        "mdi:thermometer", device_class="temperature"),
    'temp_low_2d': WUDailySimpleForecastSensorConfig(
        "Low Temperature Tomorrow", 3, "temperature", TEMPUNIT,
        "mdi:thermometer", device_class="temperature"),
    'temp_low_3d': WUDailySimpleForecastSensorConfig(
        "Low Temperature in 3 Days", 5, "temperature", TEMPUNIT,
        "mdi:thermometer", device_class="temperature"),
    'temp_low_4d': WUDailySimpleForecastSensorConfig(
        "Low Temperature in 4 Days", 7, "temperature", TEMPUNIT,
        "mdi:thermometer", device_class="temperature"),
    'temp_low_5d': WUDailySimpleForecastSensorConfig(
        "Low Temperature in 5 Days", 9, "temperature", TEMPUNIT,
        "mdi:thermometer", device_class="temperature"),
    'wind_1d': WUDailySimpleForecastSensorConfig(
        "Avg. Wind Today", 0, "windSpeed", SPEEDUNIT,
        "mdi:weather-windy"),
    'wind_2d': WUDailySimpleForecastSensorConfig(
        "Avg. Wind Tomorrow", 2, "windSpeed", SPEEDUNIT,
        "mdi:weather-windy"),
    'wind_3d': WUDailySimpleForecastSensorConfig(
        "Avg. Wind in 3 Days", 4, "windSpeed", SPEEDUNIT,
        "mdi:weather-windy"),
    'wind_4d': WUDailySimpleForecastSensorConfig(
        "Avg. Wind in 4 Days", 6, "windSpeed", SPEEDUNIT,
        "mdi:weather-windy"),
    'wind_5d': WUDailySimpleForecastSensorConfig(
        "Avg. Wind in 5 Days", 8, "windSpeed", SPEEDUNIT,
        "mdi:weather-windy"),
    'precip_1d': WUDailySimpleForecastSensorConfig(
        "Precipitation Intensity Today", 0, 'qpf', LENGTHUNIT,
        "mdi:umbrella"),
    'precip_2d': WUDailySimpleForecastSensorConfig(
        "Precipitation Intensity Tomorrow", 2, 'qpf', LENGTHUNIT,
        "mdi:umbrella"),
    'precip_3d': WUDailySimpleForecastSensorConfig(
        "Precipitation Intensity in 3 Days", 4, 'qpf', LENGTHUNIT,
        "mdi:umbrella"),
    'precip_4d': WUDailySimpleForecastSensorConfig(
        "Precipitation Intensity in 4 Days", 6, 'qpf', LENGTHUNIT,
        "mdi:umbrella"),
    'precip_5d': WUDailySimpleForecastSensorConfig(
        "Precipitation Intensity in 5 Days", 8, 'qpf', LENGTHUNIT,
        "mdi:umbrella"),
    'precip_chance_1d': WUDailySimpleForecastSensorConfig(
        "Precipitation Probability Today", 0, "precipChance", PERCENTAGEUNIT,
        "mdi:umbrella"),
    'precip_chance_2d': WUDailySimpleForecastSensorConfig(
        "Precipitation Probability Tomorrow", 2, "precipChance", PERCENTAGEUNIT,
        "mdi:umbrella"),
    'precip_chance_3d': WUDailySimpleForecastSensorConfig(
        "Precipitation Probability in 3 Days", 4, "precipChance", PERCENTAGEUNIT,
        "mdi:umbrella"),
    'precip_chance_4d': WUDailySimpleForecastSensorConfig(
        "Precipitation Probability in 4 Days", 6, "precipChance", PERCENTAGEUNIT,
        "mdi:umbrella"),
    'precip_chance_5d': WUDailySimpleForecastSensorConfig(
        "Precipitation Probability in 5 Days", 8, "precipChance", PERCENTAGEUNIT,
        "mdi:umbrella"),
}

WEATHER_SYMBOL_TO_HASS = {
    0: ATTR_CONDITION_SUNNY,
    1: ATTR_CONDITION_PARTLYCLOUDY,
    2: ATTR_CONDITION_PARTLYCLOUDY,
    3: ATTR_CONDITION_CLOUDY,
    4: ATTR_CONDITION_CLOUDY,
    5: ATTR_CONDITION_CLOUDY,
    6: ATTR_CONDITION_RAINY,
    7: ATTR_CONDITION_SNOWY_RAINY,
    8: ATTR_CONDITION_POURING,
    9: ATTR_CONDITION_HAIL,
    10: ATTR_CONDITION_SNOWY,
    11: ATTR_CONDITION_SNOWY,
    12: ATTR_CONDITION_SNOWY_RAINY,
    13: "snowy-heavy",
    14: ATTR_CONDITION_HAIL,
    15: ATTR_CONDITION_LIGHTNING_RAINY,
    16: ATTR_CONDITION_WINDY,
    17: "tornado",
    18: ATTR_CONDITION_FOG,
    19: "hazy",
    20: "hazy",
    21: "hazy",
    -2: None,
}
