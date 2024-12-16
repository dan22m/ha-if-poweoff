from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from .sensor import PowerOffCoordinator

class IfPoweroffConfigFlow(config_entries.ConfigFlow, domain="if_poweroff"):
    """Конфігурація інтеграції через інтерфейс Home Assistant."""

    async def async_step_user(self, user_input=None):
        """Запитуємо ім'я та налаштовуємо інтеграцію."""
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME, default="Ivano-Frankivsk Power Off"): str,
                }
            ),
        )
