import random

path_conditions = []


class Linear:
    def __init__(self, coeffs: dict[str, int]):
        self.coeffs = coeffs

    def __ge__(self, other):
        result = random.choice([True, False])
        if result:
            path_conditions.append(f"{self} >= {other}")
        else:
            path_conditions.append(f"{self} < {other}")
        return result

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
c = Linear({"c": 1})


def run(func, *args):
    path_conditions.clear()
    result = func(*args)
    print("Path conditions:")
    for pc in path_conditions:
        print(f"  {pc}")
    print()
    print("Result:")
    print(f"  {result}")
    print()
    print()


def max2(x, y):
    if x >= y:
        return x
    else:
        return y


run(max2, a, b)


def clamp(x, low, high):
    if x >= high:
        return high
    elif x >= low:
        return x
    else:
        return low


run(clamp, a, 5, 10)


def max3(x, y, z):
    if x >= y:
        return max2(x, z)
    else:
        return max2(y, z)


run(max3, a, b, c)


def remainder(x, y):
    while x >= y:
        x = x - y
    return x


run(remainder, a, b)


def divide(x, y):
    q = 0
    while x >= y:
        x = x - y
        q = q + 1
    return q


run(divide, a, b)
