import ledger
from Account import Account

import subprocess # ONCE LEDGER MODULE IS WORKING, REMOVE THIS
from typing import List, Optional

class Ledger:
    def __init__(self, ledger_file: str):
        """
        Initialize the Ledger class with the main ledger file.
        
        :param ledger_file: Path to the ledger file (e.g., 'xxx.ledger')
        """
        self.ledger_file = ledger_file
        self.journal = ledger.read_journal(ledger_file)
        self.accounts = {}

    def populate_accounts(self):
        """
        Populate Account objects from the ledger journal.
        """
        for xact in self.journal.xacts():
            for post in xact.posts():
                account_name = post.account.fullname()
                if account_name not in self.accounts:
                    self.accounts[account_name] = Account(account_name)

                # Build parent child relationships
                parts = account_name.split(":")
                for i in range(1, len(parts)):
                    parent_name = ":".join(parts[:i])
                    child_name = ":".join(parts[:i + 1])
                    if parent_name not in self.accounts:
                        self.accounts[parent_name] = Account(parent_name)
                    if child_name not in self.accounts:
                        self.accounts[child_name] = Account(child_name)

                    parent_account = self.accounts[parent_name]
                    child_account = self.accounts[child_name]

                    parent_account.add_child(child_account)
                    child_account.set_parent(parent_account)

                self.accounts[account_name].add_transaction(post)

    def get_account(self, name:str):
        """
        Retrieve an Account object by name.

        :param name: The full name of the account.
        :return: The Account object, or None if not found.
        """
        return self.accounts.get(name)

    def top_level_accounts(self):
        """
        Get all top-level accounts (those without parents).

        :return: A list of top-level Account objects.
        """
        return [account for account in self.accounts.values() if account.is_top_level]

    def __repr__(self):
        return f"Ledger(ledger_file={self.ledger_file}, accounts={len(self.accounts)})"



# OLD FUNCTIONS, SAVED FOR POSTERITY. Deprecated.
    def OLD_run_command(self, *args: str) -> str:
        """
        Run a ledger-cli command on the specified ledger file.
        
        :param args: Additional arguments for the ledger command.
        :return: Output of the command.
        """
        try:
            result = subprocess.run(
                ["ledger", "-f", self.ledger_file] + list(args),
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error running command: {' '.join(e.cmd)}")
            print(f"Error output: {e.stderr.strip()}")
            raise


    def OLD_get_accounts(self) -> List[str]:
        """
        Get all accounts from the ledger file.
        
        :return: A list of account names.
        """
        accounts_output = self.OLD_run_command("accounts")
        # Split the output into lines and return as a list
        return accounts_output.split("\n")

    def OLD_balance(self, account: Optional[str] = None) -> dict:
        """
        Get the balance of the ledger or a specific account as a dictionary.

        :param account: The account to query (optional).
        :return: A dictionary where keys are account names and values are balances.
        """
        command = ["bal", "--format", "%(account)\t%(amount)\n"]
        if account:
            command.append(account)

        output = self.OLD_run_command(*command)
        
        # Process the output into a dictionary
        balances = {}
        for line in output.splitlines():
            parts = line.split("\t")  # Split into account name and balance
            if len(parts) == 2:
                account_name, balance = parts
                balances[account_name.strip()] = balance.strip()
        
        return balances


