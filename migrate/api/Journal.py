import ledger
from Account import Account

from typing import List, Optional
from datetime import date

class Journal:
    def __init__(self, ledger_file):
        self.j = ledger.read_journal(ledger_file)
        self.accounts = self._fetch_accounts()

    def _fetch_accounts(self) -> dict[str, Account]:
        accounts = {}
        
        for xact in self.j.xacts():
            for post in xact.posts():
                account = post.account
                if account.fullname() not in accounts:
                    accounts[account.fullname()] = Account(account)

                # Traverse parent accounts
                parent_account = account.parent
                while parent_account:
                    if parent_account.fullname() not in accounts:
                        accounts[parent_account.fullname()] = Account(parent_account)
                    parent_account = parent_account.parent
                    
        return accounts

    def get_account(self, account_name: str) -> Account | None:
        if account_name in self.accounts:
            return self.accounts.get(account_name)
        else:
            raise(ValueError(f"No known account: {account_name}"))

    def get_children(self, account_name: str) -> list[Account]:
        account = self.get_account(account_name)
        if not account:
            return []

        return [
            child
            for child in self.accounts.values()
            if child.ledger_account.parent
            and child.ledger_account.parent.fullname() == account_name
        ]

    def get_balance(self, account_name: str, start_date: Optional[date] = None, end_date: Optional[date] = None) -> float:
        account = self.get_account(account_name)
        if not account:
            return 0.0

        if not start_date and not end_date:
            direct_balance = account.balance
            child_balances = sum(self.get_balance(child.fullname) for child in self.get_children(account_name))
        else:
            if not start_date:
                start_date = min(
                    (tx.date for tx in account.transactions),
                    default=date.today()
                )
            if not end_date:
                end_date = date.today()

            direct_balance = account.balance_date_filter(start_date, end_date)
            child_balances = sum(
                self.get_balance(child.fullname, start_date, end_date)
                for child in self.get_children(account_name)
            )
            
        return direct_balance + child_balances


