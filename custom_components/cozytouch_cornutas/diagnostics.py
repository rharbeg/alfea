"""Diagnostics support for the Cozytouch integration."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry

from .const import DOMAIN


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, config_entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    hub = hass.data[DOMAIN][config_entry.entry_id]

    diagnostics: dict[str, Any] = {}

    raw_setup = hub.get_last_raw_setup()
    if raw_setup is not None:
        diagnostics["setup"] = raw_setup

    device_id = config_entry.data.get("deviceId")
    raw_device = None
    if device_id is not None:
        raw_device = hub.get_device_raw_data(device_id)

    if raw_device:
        diagnostics["device"] = raw_device

    return diagnostics


async def async_get_device_diagnostics(
    hass: HomeAssistant, config_entry: ConfigEntry, device: DeviceEntry
) -> dict[str, Any]:
    """Return diagnostics for a device."""
    return await async_get_config_entry_diagnostics(hass, config_entry)
