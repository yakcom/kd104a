from . import effects
from .enums import Direction


class Lighting:
    def __init__(self, device):
        self.device = device

        self._brightness = 50
        self._prev_brightness = 50
        self._speed = 50
        self._direction = Direction.LEFT_RIGHT

        self._mode = effects.static
        self._kwargs = {"color": (0, 0, 0)}

    def _send(self):
        kwargs = {
            "brightness": self._brightness,
            **self._kwargs,
        }

        varnames = self._mode.__code__.co_varnames

        if "speed" in varnames:
            kwargs["speed"] = self._speed

        if "direction" in varnames:
            kwargs["direction"] = self._direction

        self.device.send(self._mode(**kwargs))

    def on(self):
        self._brightness = self._prev_brightness
        self._send()

    def off(self):
        self._prev_brightness = self._brightness
        self._brightness = 0
        self._send()

    def set_mode(
        self,
        mode,
        *,
        brightness=None,
        speed=None,
        direction=None,
        **kwargs,
    ):
        self._mode = mode

        if brightness is not None:
            self._brightness = brightness
        if speed is not None:
            self._speed = speed
        if direction is not None:
            self._direction = direction

        self._kwargs = kwargs
        self._send()

    def set_brightness(self, value: int):
        self._brightness = value
        self._send()

    def set_speed(self, value: int):
        self._speed = value
        self._send()

    def set_direction(self, value: Direction):
        self._direction = value
        self._send()