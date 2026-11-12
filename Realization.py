from abc import ABC, abstractmethod

class PayCard(ABC):
    @abstractmethod
    def processing_payment(self, amount: float) -> bool:
        pass

class DebitPayment(PayCard):
    def processing_payment(self, amount: float) -> bool:
        print(f'Processing P{amount}')  
        return True


Card1 = DebitPayment()

success = Card1.processing_payment(264.32)
print(f'Payment successful: {success}')
