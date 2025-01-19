import subprocess
from typing import List, Optional

class Ledger:
    def __init__(self, ledger_file: str):
        """
        Initialize the Ledger class with the main ledger file.
        
        :param ledger_file: Path to the ledger file (e.g., 'xxx.ledger')
        """
        self.ledger_file = ledger_file

    def run_command(self, *args: str) -> str:
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


    def get_accounts(self) -> List[str]:
        """
        Get all accounts from the ledger file.
        
        :return: A list of account names.
        """
        accounts_output = self.run_command("accounts")
        # Split the output into lines and return as a list
        return accounts_output.split("\n")

    def balance(self, account: Optional[str] = None) -> dict:
        """
        Get the balance of the ledger or a specific account as a dictionary.

        :param account: The account to query (optional).
        :return: A dictionary where keys are account names and values are balances.
        """
        command = ["bal", "--format", "%(account)\t%(amount)\n"]
        if account:
            command.append(account)

        output = self.run_command(*command)
        
        # Process the output into a dictionary
        balances = {}
        for line in output.splitlines():
            parts = line.split("\t")  # Split into account name and balance
            if len(parts) == 2:
                account_name, balance = parts
                balances[account_name.strip()] = balance.strip()
        
        return balances
