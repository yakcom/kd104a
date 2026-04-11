import hid


class Device:
    def __init__(
        self,
        product: str | None = None,
        manufacturer: str | None = None,
        vid: int | None = None,
        pid: int | None = None,
        interface: int | None = None,
        usage_page: int | None = None,
    ):
        dev = next(
            (
                d
                for d in hid.enumerate()
                if (product is None or (d["product_string"] or "") == product)
                and (manufacturer is None or (d["manufacturer_string"] or "") == manufacturer)
                and (vid is None or d["vendor_id"] == vid)
                and (pid is None or d["product_id"] == pid)
                and (interface is None or d["interface_number"] == interface)
                and (usage_page is None or d["usage_page"] == usage_page)
            ),
            None,
        )

        if dev is None:
            raise RuntimeError("Device not found")

        self.path = dev["path"]

    def send(self, packet: bytes):
        device = hid.device()
        try:
            device.open_path(self.path)
            written = device.write(packet)
            if written != len(packet):
                raise RuntimeError(f"Failed to write full packet: {written}/{len(packet)} bytes")
        finally:
            device.close()