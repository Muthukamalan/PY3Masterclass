class BankAccount:
    def __init__(self, owner: str, initial_balance: float):
        self.owner = owner
        # Private attributes (encapsulated; not meant to be touched directly)
        self.__balance = initial_balance
        self.__pin = 1234

    # Encapsulated behavior: controlled access via methods
    def deposit(self, amount: float) -> float:
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit must be positive")
        return self.__balance

    def withdraw(self, amount: float, pin: int) -> float:
        if pin != self.__pin:
            raise ValueError("Wrong PIN")
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError("Not enough balance")
        self.__balance -= amount
        return self.__balance

    def get_balance(self) -> str:
        # Getter that hides the raw attribute
        return f"Account holder: {self.owner}, Balance: ${self.__balance}"