# kd104a
Simple HID control for KD104A keyboard lighting.

# Install

```bash
pip install kd104a
```

# Quick Start

```python
from kd104a import Device, Lighting, Direction, effects

keyboard = Device(product="Gaming Keyboard", interface=2)
lighting = Lighting(keyboard)

lighting.set_mode(
    effects.wave,
    brightness=1,
    speed=20,
    direction=Direction.RIGHT_LEFT,
    color1="red",
    color2="blue",
)
```

# Usage

### Power

```python
lighting.off()
lighting.on()
```

### Change mode

```python
lighting.set_mode(effects.static, color="yellow")
```

### Update parameters

```python
lighting.set_brightness(100)
lighting.set_speed(10)
lighting.set_direction(Direction.LEFT_RIGHT)
```

# Parameters

### Brightness / Speed

```python
0-100  # percent
```

# Colors

```python
"red"
"#ff0000"
(255, 0, 0)
```

# Direction

```python
Direction.LEFT_RIGHT
Direction.RIGHT_LEFT
Direction.TOP_BOTTOM
Direction.BOTTOM_TOP
Direction.CENTER_OUT
Direction.OUT_CENTER
Direction.CLOCKWISE
Direction.COUNTER_CLOCKWISE
```

# Effects

```python
effects.static
effects.neon
effects.breathing
effects.wave
effects.blink
effects.radar
effects.ripple
effects.marquee
effects.shine
effects.ripple2
effects.interactive
effects.crossing
effects.firework
effects.reactive
effects.equalizer
```