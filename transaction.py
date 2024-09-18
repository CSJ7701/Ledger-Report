import re
from datetime import datetime

class Transaction:
    def __init__(self, date, code, payee, account, currency, amount, cleared, notes):
        self.date=datetime.strptime(date, "yyyy/mm/dd")
        self.code=code
        self.payee=payee
        self.account=self.get_account_name(account)
        self.category=self.get_account_category(account)
        self.currency=currency
        self.amount=amount
        self.cleared=self.is_cleared(cleared)
        self.tags=self.get_tags(notes)
        

    def get_account_name(self, account_string: str) -> str:
        account_list=account_string.split(":")
        return account_list[-1]

    def get_account_category(self, account_str: str) -> str:
        parts=account_str.rsplit(':', 1)
        return parts[0] if len(parts) > 1 else account_str

    def is_cleared(self, cleared: str) -> bool:
        return cleared == "*"

    def get_tags(self, notes: str) -> list[str]:

        # Define patterns for the three formats
        pattern_colon_text_colon = re.compile(r':([^:]+):')
        pattern_text_colon_text = re.compile(r'\b[^:\s]+:\s[^:\s]+\b')
    
        results = []

        # Split the input string by spaces
        elements = notes.split()

        for element in elements:
            if pattern_colon_text_colon.match(element):
                # Extract text between colons
                match = pattern_colon_text_colon.match(element)
                results.append(match.group(1))
            elif pattern_text_colon_text.match(element):
            # Add the entire 'text: text' string
                results.append(element)

        return results
