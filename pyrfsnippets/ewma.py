import copy


class EWMA:
    """Exponentially-weighted moving average

    vals: Number, or list of numbers to add
    weight: Moving average weight, default 8.0
    """
    _state = 0.0
    weight = 8.0
    items = 0

    def __init__(self, vals=None, weight=8.0):
        self.weight = weight
        if vals is not None:
            self.add(vals)

    def __add__(self, vals):
        c = copy.copy(self)
        c.add(vals)
        return c

    def __len__(self):
        return self.items

    def __float__(self):
        return self.average

    def __int__(self):
        return int(self.average)

    def add(self, vals):
        """Add one or more numbers to the weighted average, in place

        vals: Number, or list of numbers
        """
        if isinstance(vals, (int, float, complex)):
            vals = [vals]
        for number in vals:
            if self._state == 0.0:
                self._state = number * self.weight
            else:
                self._state += (number - (self._state / self.weight))
            self.items += 1

    def append(self, vals):
        self.add(vals)

    def extend(self, vals):
        self.add(vals)

    def copy(self):
        return copy.copy(self)

    @property
    def average(self):
        """Weighted average of the current EWMA set"""
        return self._state / self.weight
