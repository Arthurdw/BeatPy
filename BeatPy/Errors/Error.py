class BeatPy(Exception):
    """Base exception for BeatPy!
    This will catch all the BeatPy exceptions!"""
    pass


class CoreError(BeatPy):
    """Library Core error.
    If this pops please create a issue at:
    https://github.com/Arthurdw/BeatPy/issues"""
    pass


class FormatError(BeatPy):
    """Occurs when you want something to be created but its missing something."""
    pass
