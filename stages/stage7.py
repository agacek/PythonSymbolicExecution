forced_choices = []
actual_choices = []


def choose() -> bool:
    i = len(actual_choices)
    if i < len(forced_choices):
        result = forced_choices[i]
    else:
        result = False

    actual_choices.append(result)
    return result


def force_next_choice():
    if False not in actual_choices:
        raise StopIteration

    while actual_choices[-1]:
        actual_choices.pop()

    actual_choices[-1] = True
    forced_choices[:] = actual_choices


path_conditions = []


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


def run_all(func, *args):
    forced_choices.clear()

    try:
        for _ in range(10):
            actual_choices.clear()
            run(func, *args)
            force_next_choice()
    except StopIteration:
        print("Done")


class Linear:
    def __init__(self, coeffs: dict[str, int]):
        self.coeffs = coeffs

    def __ge__(self, other):
        result = choose()
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


def max2(x, y):
    if x >= y:
        return x
    else:
        return y


def clamp(x, low, high):
    if x >= high:
        return high
    elif x >= low:
        return x
    else:
        return low


def remainder(x, y):
    while x >= y:
        x = x - y
    return x


def divide(x, y):
    q = 0
    while x >= y:
        x = x - y
        q = q + 1
    return q


run_all(max2, a, b)
run_all(clamp, a, 5, 10)
run_all(remainder, a, b)
run_all(divide, a, b)
