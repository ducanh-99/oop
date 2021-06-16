class Card:
    __balance: int

    _name: str

    def __init__(self, balance=0, name="My") -> None:
        self.__balance = balance

    def get_balance(self):
        return self.__balance


class CreditCard(Card):

    def __init__(self, name = "My") -> None:
        self._name = name

    def get_name(self):
        print(self.__balance)
        return self._name


credit_card = CreditCard()
print(credit_card.get_name())

# card = Card()
# # print(card.__balance)
# # print(card.get_balance())
# print(card._name)
