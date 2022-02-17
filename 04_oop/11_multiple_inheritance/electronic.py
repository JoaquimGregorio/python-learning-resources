class Electronic:
    def __init__(self, name: str) -> None:
        self._name = name
        self._switched_on = False

    def switch_on(self):
        if self._switched_on:
            return
        self._switched_on = True

    def switch_off(self):
        if not self._switched_on:
            return
        self._switched_on = False
