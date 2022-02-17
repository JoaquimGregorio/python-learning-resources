from electronic import Electronic
from log import LogMixin


class Smartphone(Electronic, LogMixin):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._connected = False

    def connect(self):
        if not self._switched_on:
            error = f"{self._name} is not switched on."
            self.log_error(error)
            print(error)
            return
        if self._connected:
            error = f"{self._name} is already connected."
            self.log_error(error)
            print(error)
            return

        self._connected = True
        info = f"{self._name} is connected."
        self.log_info(info)
        print(info)

    def disconnect(self):
        if not self._connected:
            error = f"{self._name} is already not connected."
            self.log_error(error)
            print(error)
            return
        self._connected = False
        info = f"{self._name} is not connected."
        self.log_info(info)
        print(info)
