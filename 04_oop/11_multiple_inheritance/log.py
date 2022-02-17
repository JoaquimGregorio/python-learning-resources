class LogMixin:
    @staticmethod
    def write(msg: str):
        with open("log.log", "a+") as log_file:
            log_file.write(msg)
            log_file.write("\n")
            log_file.close()

    def log_info(self, msg: str):
        self.write(f"INFO: {msg}")

    def log_error(self, msg: str):
        self.write(f"ERROR: {msg}")
