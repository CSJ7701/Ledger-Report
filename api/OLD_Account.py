class Account:
    def __init__(self, name:str):
        """
        Initialize an Account object.

        :param name: The name of the account.
        :param balance: The balance of the account.
        """
        self.name = name
        self.parent = None
        self.children = set()
        self.transactions = []

    def set_parent(self, parent):
        """Set the parent for this account."""
        self.parent = parent

    def add_child(self, child):
        """Add a child account."""
        self.children.add(child)

    def add_transaction(self, transaction):
        """
        Add a transaction (posting) to this account.

        :param transaction: A ledger posting object.
        """
        self.transactions.append(transaction)

    def calculate_balance(self, include_subaccounts=True):
        """
        Calculate the balance for this account.

        :param include_subaccounts: If True, include balances of child accounts.
        :return: The total balance for the account.
        """
        balance = sum(post.amount.to_double() for post in self.transactions)

        if include_subaccounts:
            for child in self.children:
                balance += child.calculate_balance()

        return balance

    @property
    def top_level_name(self):
        """Get the top level name of the account (e.g., 'Expenses' for 'Expenses:Food:Groceries'."""
        return self.name.split(":")[0]

    @property
    def is_top_level(self):
        """Check if this account is a top-level account (i.e., no parent)"""
        return ":" not in self.name

    @property
    def direct_parent_name(self):
        """Get the immediate parent's name (e.g., 'Expenses:Food' for 'Expenses:Food:Groceries'."""
        if self.is_top_level:
            return None
        return ":".join(self.name.split(":")[:-1])

    @property
    def child_names(self):
        return [child.name for child in self.children]

    
    def __repr__(self):
        if self.is_top_level:
            return f"Account(name={self.name}, children={len(self.children)})"
        else:
            return f"Account(name={self.name}, balance={self.calculate_balance()}, parent={self.parent.name if self.parent else None}, children={len(self.children)})"
