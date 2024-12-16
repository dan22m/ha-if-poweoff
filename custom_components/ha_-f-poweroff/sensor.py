import logging
import requests
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

_LOGGER = logging.getLogger(__name__)

# Функція для отримання даних з API
def get_power_off_data():
    url = "https://if-svitlo-api.dan.org.ua/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Перевірка на помилки
        data = response.json()  # Отримуємо дані у форматі JSON
        return data
    except requests.exceptions.RequestException as e:
        _LOGGER.error("Error fetching data from API: %s", e)
        return None


class PowerOffCoordinator(DataUpdateCoordinator):
    """Координатор для отримання даних про вимкнення електроенергії."""

    def __init__(self, hass, update_interval):
        """Ініціалізація координатора."""
        self._update_interval = update_interval
        super().__init__(
            hass,
            _LOGGER,
            name="Power Off Coordinator",
            update_interval=timedelta(minutes=update_interval),
        )

    async def _async_update_data(self):
        """Отримуємо дані з API."""
        data = await self.hass.async_add_executor_job(get_power_off_data)
        if not data:
            raise UpdateFailed("Error fetching data")
        return data


class PowerOffSensor(SensorEntity):
    """Інтеграція для створення сенсора Power Off."""

    def __init__(self, coordinator):
        """Ініціалізація сенсора."""
        self._coordinator = coordinator
        self._state = None

    @property
    def name(self):
        """Ім'я сенсора."""
        return "Ivano-Frankivsk Power Off Sensor"

    @property
    def state(self):
        """Статус сенсора."""
        return self._state

    async def async_update(self):
        """Оновлюємо дані сенсора."""
        data = await self._coordinator.async_refresh()
        # Отримуємо статус вимкнення електрики для поточної години
        self._state = data.get("today", {}).get("status", "No data")
