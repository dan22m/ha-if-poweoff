from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .sensor import PowerOffSensor, PowerOffCoordinator
import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Налаштування компоненту."""
    _LOGGER.info("Setting up Ivano-Frankivsk Power Off integration")

    # Створення координатора для отримання даних
    coordinator = PowerOffCoordinator(hass, update_interval=30)

    # Створення сенсора для отримання статусу
    hass.data["if_poweroff"] = PowerOffSensor(coordinator)

    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Налаштування при додаванні конфігураційного запису."""
    return await async_setup(hass, {})

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Видалення інтеграції."""
    return True
