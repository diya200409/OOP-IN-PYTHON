from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


# Child Class 1
class UPI(Payment):

    def pay(self):
        print("Payment done using UPI")


# Child Class 2
class CreditCard(Payment):

    def pay(self):
        print("Payment done using Credit Card")


# Child Class 3
class NetBanking(Payment):

    def pay(self):
        print("Payment done using Net Banking")


# Creating Objects
upi = UPI()
card = CreditCard()
net = NetBanking()

# Calling Methods
upi.pay()
card.pay()
net.pay()