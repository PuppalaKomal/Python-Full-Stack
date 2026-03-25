from database import DatabaseConfig
class Balance:
    def __init__(self, account):
        self.account = account
    def get_balance(self):
        try:
            db_config = DatabaseConfig()
            cursor = db_config.cursor()
            get_balance_query = """SELECT balance FROM accounts WHERE account = %s;"""
            cursor.execute(get_balance_query, (self.account,))
            amount = cursor.fetchone()[0]
            return f"Your current balance is {amount}"
        except Exception as e:
            return f"Something wrong with bank/balance.py: {e}"
