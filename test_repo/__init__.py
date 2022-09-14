class A:
    def __init__(self) -> None:
        pass

    def __add__(self, other):
        raise NotImplementedError
    def __test__(self):
        ...

    def test():
        ...


def add(a:int, b: int) -> bool:
    return a +b

add("1", 2)

a=A()
def wrong_callable():
    if hasattr(a, "__call__"):
        return a()
