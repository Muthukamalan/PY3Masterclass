# Abstraction 
# Abstraction is the process of hiding complex implementation details and exposing only the essential functionality



from abc import ABC, abstractmethod
from uuid import UUID

class Payment(ABC):
    """The Abstract Base Class"""
    pay_id: UUID  # Shared attribute

    @abstractmethod
    def make_payment(self, amount):
        """Docstring for make_payment with no implementation"""
        pass 



# Concrete Classes
class CreditCardPayment(Payment):
    def make_payment(self, amount):
        """Implementation of Contreter Class"""
        print(f"Paid {amount} using Credit Card")

class UpiPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} via UPI")



if __name__=="__main__":
    cc_payment = CreditCardPayment()
    cc_payment.make_payment(1000)




# Base Class
# https://github.com/huggingface/transformers/blob/380e3cc5d59912a48508cb6d4959a31cd460e12e/src/transformers/generation/continuous_batching/cb_logits_processors.py#L28
# Concrete Class
# https://github.com/huggingface/transformers/blob/380e3cc5d59912a48508cb6d4959a31cd460e12e/src/transformers/generation/continuous_batching/cb_logits_processors.py#L214
