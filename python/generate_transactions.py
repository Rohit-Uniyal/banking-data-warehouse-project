import pandas as pd
import random
from datetime import datetime, timedelta

accounts = pd.read_csv("../data/raw/accounts.csv")

transactions = []

transaction_id = 1

transaction_types = [
    "Deposit",
    "Withdrawal",
    "UPI",
    "NEFT",
    "IMPS",
    "Salary Credit"
]

for _, account in accounts.iterrows():

    num_transactions = random.randint(10, 30)

    for _ in range(num_transactions):

        random_days = random.randint(1, 365)

        transaction_date = (
            datetime.now()
            - timedelta(days=random_days)
        )

        transactions.append({
            "transaction_id": transaction_id,
            "account_id": account["account_id"],
            "transaction_type":
                random.choice(transaction_types),
            "amount":
                random.randint(100, 50000),
            "transaction_date":
                transaction_date.strftime("%Y-%m-%d")
        })

        transaction_id += 1

df_transactions = pd.DataFrame(transactions)

df_transactions.to_csv(
    "../data/raw/transactions.csv",
    index=False
)

print(
    f"{len(df_transactions)} transactions generated"
)



