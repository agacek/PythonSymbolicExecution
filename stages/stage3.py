def swap(x, y):
    x = x + y
    y = x - y
    x = x - y
    return (x, y)


class Sym:
    def __init__(self, value: str):
        self.value = value

    def __add__(self, other):
        return Sym(f"({self} + {other})")

    def __sub__(self, other):
        return Sym(f"({self} - {other})")

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"SymbolicValue[{self}]"


a = Sym("a")
b = Sym("b")

swap(a, b)
