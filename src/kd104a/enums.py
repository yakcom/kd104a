from enum import IntEnum

class Mode(IntEnum):
    STATIC = 0x00
    NEON = 0x03
    BREATHING = 0x01
    WAVE = 0x02
    BLINK = 0x04
    RADAR = 0x05
    RIPPLE = 0x06
    MARQUEE = 0x07
    SHINE = 0x08
    RIPPLE2 = 0x09
    INTERACTIVE = 0x0A
    CROSSING = 0x0B
    FIREWORK = 0x0C
    REACTIVE = 0x0D
    EQUALIZER = 0x0E

class Direction(IntEnum):
    RIGHT_LEFT = 0
    LEFT_RIGHT = 1
    BOTTOM_TOP = 2
    TOP_BOTTOM = 3
    CENTER_OUT = 4
    OUT_CENTER = 5
    CLOCKWISE = 6
    COUNTER_CLOCKWISE = 7