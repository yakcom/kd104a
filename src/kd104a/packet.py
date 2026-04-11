HEADER = (0x01, 0x07, 0x00, 0x00, 0x00, 0x0E)
PACKET_SIZE = 64


def build_packet(
    mode: int,
    brightness: int = 0,
    speed: int = 0,
    color1=(0, 0, 0),
    color2=(0, 0, 0),
    direction: int = 0,
    palette: int = 0,
) -> bytes:
    buf = [0] * PACKET_SIZE
    buf[0:6] = HEADER
    buf[6] = int(mode)
    buf[7] = brightness
    buf[8] = speed
    buf[9:12] = color1
    buf[12:15] = color2
    buf[15] = direction
    buf[16] = palette
    return bytes(buf)