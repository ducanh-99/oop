class RealNumber:

    real: float
    vitural: float

    def __init__(self, real, vitural) -> None:
        self.real = real
        self.vitural = vitural

    def __add__(self, real_number):
        return RealNumber(self.real + real_number.real, self.vitural + real_number.vitural)


a = RealNumber(1, 1)
b = RealNumber(1, 2)
c = a + b
print(c.real, c.vitural)
