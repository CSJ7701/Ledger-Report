from _typeshed import DataclassInstance


class Transaction:
    def __init__(self, date: str, payee: str, amount: str, account:str):
        """
        Initialize a Transaction object.

        :param date: Date of the transaction.
        :param payee: Payee of the transaction.
        :param amount: Amount of the transaction.
        :param account: Account associated with the transaction.
        """

        self.date = date
        self.payee = payee
        self.amount = amount
        self.account = account

    def __repr__(self):
        return f"Transaction(date={self.date}, payee={self.payee}, amount={self.amount}, account={self.account})"
