class A:
    def __init__(self) -> None:
        print("a")


class B(A):

    def __init__(self) -> None:
        super().__init__()
        print("b")


class C(B):

    def __init__(self) -> None:
        super().__init__()
        print("c")

c = C()