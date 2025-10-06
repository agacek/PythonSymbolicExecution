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
    actual_choices.clear()
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
            run(func, *args)
            force_next_choice()
    except StopIteration:
        print("Done")


class Sym:
    def __init__(self, value: str):
        self.value = value

    def __getitem__(self, key: str):
        item = f"{self}['{key}']"
        if choose():
            path_conditions.append(f"{item} exists")
            return Sym(item)
        else:
            path_conditions.append(f"{item} does not exist")
            raise KeyError

    def __bool__(self) -> bool:
        if choose():
            path_conditions.append(f"{self} is True")
            return True
        else:
            path_conditions.append(f"{self} is False")
            return False

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"SymbolicValue[{self}]"


def pitr_enabled(props):
    try:
        if props["pitrSpec"]["pitrEnabled"]:
            return "COMPLIANT"
        else:
            return "NON_COMPLIANT"
    except KeyError:
        return "ERROR"


run_all(pitr_enabled, Sym("properties"))
