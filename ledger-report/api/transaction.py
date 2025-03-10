import ledger
import datetime

class Transaction:
    def __init__(self, posting: ledger.Posting):
        self.ledger_posting = posting
        self.ledger_transaction = posting.xact
    
    @property
    def date(self) -> datetime.date:
        return self.ledger_transaction.date

    @property
    def payee(self):
        return self.ledger_transaction.payee

    @property
    def note(self):
        return self.ledger_posting.note

    @property
    def amount(self):
        return self.ledger_posting.amount

    @property
    def cleared(self):
        return self.ledger_posting.state == ledger.state.Cleared

    def __repr__(self) -> str:
        return f"<Transaction(date={self.date}, payee={self.payee}, amount={self.amount})>"
