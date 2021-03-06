""" shared data """
from homeassistant.util import Throttle
from datetime import timedelta

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=5)

class WUndergroundData:
    """Get data from WUnderground."""

    def __init__(self, hass, api_key, pws_id, numeric_precision, unit_system_api, unit_system, lang):
        """Initialize the data object."""
        self._hass = hass
        self._api_key = api_key
        self._pws_id = pws_id
        self._numeric_precision = numeric_precision
        self._unit_system_api = unit_system_api
        self.unit_system = unit_system
        self.units_of_measurement = None
        self._lang = 'language={}'.format(lang)        
        self._features = set()
        self.data = None
        self._session = async_get_clientsession(self._hass)

        if unit_system_api == 'm':
            self.units_of_measurement = (TEMP_CELSIUS, LENGTH_MILLIMETERS, LENGTH_METERS, SPEED_KILOMETERS_PER_HOUR,
                                         PRESSURE_MBAR, PRECIPITATION_MILLIMETERS_PER_HOUR, PERCENTAGE)
        else:
            self.units_of_measurement = (TEMP_FAHRENHEIT, LENGTH_INCHES, LENGTH_FEET, SPEED_MILES_PER_HOUR,
                                         PRESSURE_INHG, PRECIPITATION_INCHES_PER_HOUR, PERCENTAGE)

    def request_feature(self, feature):
        """Register feature to be fetched from WU API."""
        self._features.add(feature)

    def _build_url(self, baseurl):
        if baseurl is _RESOURCECURRENT:
            if self._numeric_precision == 'none':
                url = baseurl.format(self._pws_id, self._unit_system_api, self._api_key)
            else:
                url = baseurl.format(self._pws_id, self._unit_system_api, self._api_key) + '&numericPrecision=decimal'
        #else:
            #url = baseurl.format(self._latitude, self._longitude, self._unit_system_api, self._lang, self._api_key)

        return url

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def async_update(self):
        """Get the latest data from WUnderground."""
        headers = {'Accept-Encoding': 'gzip'}
        try:
            with async_timeout.timeout(10):
                response = await self._session.get(self._build_url(_RESOURCECURRENT), headers=headers)
            result_current = await response.json()

            # need to check specific new api errors
            # if "error" in result['response']:
            #     raise ValueError(result['response']["error"]["description"])
            # _LOGGER.debug('result_current' + str(result_current))

            if result_current is None:
                raise ValueError('NO CURRENT RESULT')
            with async_timeout.timeout(10):
                response = await self._session.get(self._build_url(_RESOURCEFORECAST), headers=headers)
            result_forecast = await response.json()

            if result_forecast is None:
                raise ValueError('NO FORECAST RESULT')

            result = {**result_current, **result_forecast}

            self.data = result
        except ValueError as err:
            _LOGGER.error("Check WUnderground API %s", err.args)
        except (asyncio.TimeoutError, aiohttp.ClientError) as err:
            _LOGGER.error("Error fetching WUnderground data: %s", repr(err))
