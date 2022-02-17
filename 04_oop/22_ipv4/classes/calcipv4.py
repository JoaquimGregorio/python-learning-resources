import re
from typing import Union


class CalcIpv4:
    def __init__(
        self, ip: str, mask: Union[str, None] = None, prefix: Union[int, None] = None
    ):
        self.ip: str = ip
        self.mask: Union[str, None] = mask
        self.prefix: Union[int, None] = prefix

        self._set_broadcast()
        self._set_net()

    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    @property
    def prefix(self):
        return self._prefix

    @property
    def net(self):
        return self._net

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def number_of_ips(self):
        return self._get_number_of_ips()

    @ip.setter
    def ip(self, value: str):
        if not self._validate_ip(value):
            raise ValueError("Invalid IP.")

        self._ip = value
        self._bin_ip = self._ip_to_bin(value)

    @mask.setter
    def mask(self, value: str):
        if not value:
            return

        if not self._validate_ip(value):
            raise ValueError("Invalid mask.")

        self._mask = value
        self._bin_mask = self._ip_to_bin(value)

        if not hasattr(self, "prefix"):
            self.prefix = self._bin_mask.count("1")

    @prefix.setter
    def prefix(self, value: int):
        if not value:
            return

        if not isinstance(value, int):
            raise TypeError("Prefix must be an integer.")

        if value > 32:
            raise TypeError("Prefix must have 32 bits.")

        self._prefix = value
        self._bin_mask = (value * "1").ljust(32, "0")
        self.mask = self._bin_to_ip(self._bin_mask)

    @staticmethod
    def _validate_ip(ip: str):
        regexp = re.compile(r"^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$")

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip: str):
        splited_blocks = ip.split(".")
        bin_blocks = [bin(int(block))[2:].zfill(8) for block in splited_blocks]
        return "".join(bin_blocks)

    @staticmethod
    def _bin_to_ip(bin_ip: str):
        n = 8
        blocks = [str(int(bin_ip[i : n + i], 2)) for i in range(0, 32, 8)]
        return ".".join(blocks)

    def _set_broadcast(self):
        host_bits = 32 - self.prefix
        self._bin_broadcast = self._bin_ip[: self.prefix] + (host_bits * "1")
        self._broadcast = self._bin_to_ip(self._bin_broadcast)
        return self._broadcast

    def _set_net(self):
        host_bits = 32 - self.prefix
        self._bin_net = self._bin_ip[: self.prefix] + (host_bits * "0")
        self._net = self._bin_to_ip(self._bin_net)
        return self._net

    def _get_number_of_ips(self):
        return 2 ** (32 - self.prefix)
