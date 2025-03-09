import ledger
from typing import List
from datetime import date
from Transaction import Transaction

class Account:
    def __init__(self, account: ledger.Account):
        self.ledger_account = account

    @property
    def fullname(self):
        return self.ledger_account.fullname()

    @property
    def name(self):
        return self.ledger_account.name

    @property
    def parent(self):
        return self.ledger_account.parent

    @property
    def children(self) -> List[ledger.Account]:
        children = []
        for child in self.ledger_account.account():
            children.append(child.fullname())
        return children
    
    @property
    def balance(self):
        return sum(tx.amount for tx in self.transactions)

    @property
    def depth(self):
        return self.ledger_account.depth

    @property
    def transactions(self):
        return [Transaction(post) for post in self.ledger_account.posts()]

    @property
    def note(self):
        return self.ledger_account.note

    def summarize(self):
        return {
            "name":self.name,
            "balance":self.balance,
            "transactions":len(self.transactions),
            "depth":self.depth,
            "note":self.note,
        }

    def balance_date_filter(self, start_date: date, end_date: date):
        filtered_transactions = [
            tx for tx in self.transactions if start_date <= tx.date <= end_date
        ]
        return sum(tx.amount for tx in filtered_transactions)

    def __repr__(self):
        return f"<Account(name={self.name}, balance={self.balance}, parent={self.parent})>"
