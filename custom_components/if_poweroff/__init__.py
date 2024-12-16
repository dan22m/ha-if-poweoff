from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import discovery
from homeassistant.const import CONF_NAME
from .sensor import PowerOffCoordinator, PowerOffSensor
import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Налаштування компоненту."""
    _LOGGER.info("Setting up Ivano-Frankivsk Power Off integration")

    # Створення координатора для отримання даних
    coordinator = PowerOffCoordinator(
        hass, "Ivano-Frankivsk Power Off", update_interval=30
    )

    # Налаштування сенсора
    hass.data["if_poweroff"] = PowerOffSensor(coordinator, "Ivano-Frankivsk Power Off Sensor")

    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Налаштування при додаванні конфігураційного запису"""
    return await async_setup(hass, {})

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Видалення інтеграції."""
    return True
