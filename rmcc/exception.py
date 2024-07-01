class RmccError(Exception):
    def __init__(self, arg=""):
        self.arg = arg


class UnimplementedError(RmccError):
    def __str__(self):
        return f"{self.arg} mesh code dimension is unimplemented."
