from kd104a import Device, Lighting, Direction, effects
import time

keyboard = Device(product="Gaming Keyboard", interface=2)
lighting = Lighting(keyboard)

lighting.set_mode(
    effects.static,
    brightness=1,
    speed=20,
    direction=Direction.RIGHT_LEFT,
    color1="red",
    color2="blue",
)
