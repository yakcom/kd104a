from enum import IntEnum

class Mode(IntEnum):
    STATIC = 0x00
    NEON = 0x03
    BREATHING = 0x01
    WAVE = 0x02
    BLINK = 0x09
    RADAR = 0x04
    RIPPLE = 0x0E
    MARQUEE = 0x0F
    SHINE = 0x07
    RIPPLE2 = 0x08
    INTERACTIVE = 0x06
    CROSSING = 0x0B
    FIREWORK = 0x10
    REACTIVE = 0x0C
    EQUALIZER = 0x64

class Direction(IntEnum):
    RIGHT_LEFT = 0
    LEFT_RIGHT = 1
    BOTTOM_TOP = 2
    TOP_BOTTOM = 3
    CENTER_OUT = 4
    OUT_CENTER = 5
    CLOCKWISE = 6
    COUNTER_CLOCKWISE = 7