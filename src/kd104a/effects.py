from .packet import build_packet
from .enums import Mode, Direction
import webcolors


def _color(value):
    if isinstance(value, tuple):
        if len(value) != 3:
            raise ValueError("Color tuple must have 3 elements")
        r, g, b = value
        return int(r), int(g), int(b)

    if isinstance(value, str):
        if value.startswith("#"):
            rgb = webcolors.hex_to_rgb(value)
        else:
            rgb = webcolors.name_to_rgb(value)
        return rgb.red, rgb.green, rgb.blue

    raise TypeError("Invalid color")


def _level(value: int):
    value = max(0, min(100, int(value)))
    if value == 0:
        return 0
    return max(1, int(value * 4 / 100))


def static(brightness=50, color=(0, 0, 0)):
    return build_packet(
        mode=Mode.STATIC,
        brightness=_level(brightness),
        color1=_color(color),
    )


def neon(brightness=50, speed=50, color1=(0, 0, 0), color2=(0, 0, 0), palette=False):
    return build_packet(
        mode=Mode.NEON,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        palette=int(palette),
    )


def breathing(brightness=50, speed=50, color1=(0, 0, 0), color2=(0, 0, 0), palette=False):
    return build_packet(
        mode=Mode.BREATHING,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        palette=int(palette),
    )


def wave(
    brightness=50,
    speed=50,
    color1=(0, 0, 0),
    color2=(0, 0, 0),
    palette=False,
    direction=Direction.LEFT_RIGHT,
):
    return build_packet(
        mode=Mode.WAVE,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        direction=direction,
        palette=int(palette),
    )


def blink(brightness=50, speed=50, color1=(0, 0, 0), color2=(0, 0, 0), palette=False):
    return build_packet(
        mode=Mode.BLINK,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        palette=int(palette),
    )


def radar(
    brightness=50,
    speed=50,
    color1=(0, 0, 0),
    color2=(0, 0, 0),
    palette=False,
    direction=Direction.CLOCKWISE,
):
    return build_packet(
        mode=Mode.RADAR,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        direction=direction,
        palette=int(palette),
    )


def ripple(
    brightness=50,
    speed=50,
    color1=(0, 0, 0),
    color2=(0, 0, 0),
    palette=False,
    direction=Direction.CENTER_OUT,
):
    return build_packet(
        mode=Mode.RIPPLE,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        direction=direction,
        palette=int(palette),
    )


def marquee(
    brightness=50,
    speed=50,
    color1=(0, 0, 0),
    color2=(0, 0, 0),
    palette=False,
    direction=Direction.LEFT_RIGHT,
):
    return build_packet(
        mode=Mode.MARQUEE,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        direction=direction,
        palette=int(palette),
    )


def shine(brightness=50, speed=50, color1=(0, 0, 0), color2=(0, 0, 0), palette=False):
    return build_packet(
        mode=Mode.SHINE,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        palette=int(palette),
    )


def ripple2(
    brightness=50,
    speed=50,
    color1=(0, 0, 0),
    color2=(0, 0, 0),
    palette=False,
    direction=Direction.CENTER_OUT,
):
    return build_packet(
        mode=Mode.RIPPLE2,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        direction=direction,
        palette=int(palette),
    )


def interactive(brightness=50, speed=50, color1=(0, 0, 0), color2=(0, 0, 0), palette=False):
    return build_packet(
        mode=Mode.INTERACTIVE,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        palette=int(palette),
    )


def crossing(brightness=50, speed=50, color1=(0, 0, 0), color2=(0, 0, 0), palette=False):
    return build_packet(
        mode=Mode.CROSSING,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        palette=int(palette),
    )


def firework(brightness=50, speed=50, color1=(0, 0, 0), color2=(0, 0, 0), palette=False):
    return build_packet(
        mode=Mode.FIREWORK,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        palette=int(palette),
    )


def reactive(brightness=50, speed=50, color1=(0, 0, 0), color2=(0, 0, 0), palette=False):
    return build_packet(
        mode=Mode.REACTIVE,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        palette=int(palette),
    )


def equalizer(brightness=50, speed=50, color1=(0, 0, 0), color2=(0, 0, 0), palette=False):
    return build_packet(
        mode=Mode.EQUALIZER,
        brightness=_level(brightness),
        speed=_level(speed),
        color1=_color(color1),
        color2=_color(color2),
        palette=int(palette),
    )