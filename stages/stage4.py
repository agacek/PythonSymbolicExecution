def swap(x, y):
    x = x + y
    y = x - y
    x = x - y
    return (x, y)


class Linear:
    def __init__(self, coeffs: dict[str, int]):
        self.coeffs = coeffs

    def __add__(self, other):
        if isinstance(other, Linear):
            keys = self.coeffs.keys() | other.coeffs.keys()
            coeffs = {k: self.coeffs.get(k, 0) + other.coeffs.get(k, 0) for k in keys}
            return Linear(coeffs)
        else:
            raise NotImplementedError

    def __neg__(self):
        return Linear({k: -v for k, v in self.coeffs.items()})

    def __sub__(self, other):
        return self + (-other)

    def __str__(self):
        parts = []
        for var, count in self.coeffs.items():
            if count == 0:
                pass
            elif count == 1:
                parts.append(var)
            else:
                parts.append(f"{count}{var}")
        return " + ".join(parts)

    def __repr__(self):
        return f"SymbolicValue[{self}]"


a = Linear({"a": 1})
b = Linear({"b": 1})

swap(a, b)

#
#  ^
#  |  . (1, 4)
#  |
#  |
#  |
# -------------------->
#  |        . (4, -1)
#


def rotate90(x, y):
    return -y, x


def rotate360(x, y):
    x, y = rotate90(x, y)
    x, y = rotate90(x, y)
    x, y = rotate90(x, y)
    x, y = rotate90(x, y)
    return x, y


rotate360(a, b)
