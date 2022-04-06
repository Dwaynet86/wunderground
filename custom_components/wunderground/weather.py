"""Support for displaying weather info from Wunderground API."""
from __future__ import annotations

from datetime import timedelta

from pyecobee.const import ECOBEE_STATE_UNKNOWN

from homeassistant.components.weather import (
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
    ATTR_FORECAST_WIND_BEARING,
    ATTR_FORECAST_WIND_SPEED,
    WeatherEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PRESSURE_HPA, PRESSURE_INHG, TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant

from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.util import dt as dt_util
from homeassistant.util.pressure import convert as pressure_convert

from .const import (
    DOMAIN,
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the WUnderground weather platform."""
    data = hass.data[DOMAIN]
    dev = []
    index = 1
    dev.append( WUndergroundWeather(data, "SkyWeather", index))
    async_add_entities(dev, True)


class WUndergroundWeather(WeatherEntity):
    """Representation of WUnderground weather data."""

    def __init__(self, data, name, index):
        """Initialize the WUnderground weather platform."""
        self.data = data
        self._name = name
        self._index = index
        self.weather = None

    def get_forecast(self, index, param):
        """Retrieve forecast parameter."""
        try:
            forecast = self.weather["forecasts"][index]
            return forecast[param]
        except (IndexError, KeyError) as err:
            raise ValueError from err

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def unique_id(self):
        """Return a unique identifier for the weather platform."""
        return "unique2222"

    @property
    def condition(self):
        """Return the current condition."""
        try:
            return WEATHER_SYMBOL_TO_HASS[self.get_forecast(0, "weatherSymbol")]
        except ValueError:
            return None

    @property
    def temperature(self):
        """Return the temperature."""
        try:
            return float(self.get_forecast(0, "temperature")) / 10
        except ValueError:
            return None

    @property
    def temperature_unit(self):
        """Return the unit of measurement."""
        return TEMP_FAHRENHEIT

    @property
    def pressure(self):
        """Return the pressure."""
        try:
            pressure = self.get_forecast(0, "pressure")
            if not self.hass.config.units.is_metric:
                pressure = pressure_convert(pressure, PRESSURE_HPA, PRESSURE_INHG)
                return round(pressure, 2)
            return round(pressure)
        except ValueError:
            return None

    @property
    def humidity(self):
        """Return the humidity."""
        try:
            return int(self.get_forecast(0, "relativeHumidity"))
        except ValueError:
            return None

    @property
    def visibility(self):
        """Return the visibility."""
        try:
            return int(self.get_forecast(0, "visibility")) / 1000
        except ValueError:
            return None

    @property
    def wind_speed(self):
        """Return the wind speed."""
        try:
            return int(self.get_forecast(0, "windSpeed"))
        except ValueError:
            return None

    @property
    def wind_bearing(self):
        """Return the wind direction."""
        try:
            return int(self.get_forecast(0, "windBearing"))
        except ValueError:
            return None

    @property
    def attribution(self):
        """Return the attribution."""
        if not self.weather:
            return None

        station = self.weather.get("weatherStation", "UNKNOWN")
        time = self.weather.get("timestamp", "UNKNOWN")
        return f"Ecobee weather provided by {station} at {time} UTC"

    @property
    def forecast(self):
        """Return the forecast array."""
        if "forecasts" not in self.weather:
            return None

        

    async def rest.async_update(self):
       if not rest.data:
        raise PlatformNotReady 
    
    



