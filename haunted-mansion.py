class HauntedMansion:
    """HauntedMansion class needs a spooky_ var prefix for access to its named attributes."""
    __BOO = "Booooo, only ghosts here!"

    __SPOOKY = "spooky_"

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __getattr__(self, name):
        return self.__BOO

    def __setattr__(self, name, value):
        object.__setattr__(self, self.__SPOOKY + name, value)
