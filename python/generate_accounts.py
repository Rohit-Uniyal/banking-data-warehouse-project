import pandas as pd
import random

customers = pd.read_csv("../data/raw/customers.csv")

accounts = []

account_types = [
    "Savings",
    "Current",
    "Salary"
]

account_id = 100000

for _, customer in customers.iterrows():

    num_accounts = random.randint(1, 3)

    for _ in range(num_accounts):

        accounts.append({
            "account_id": account_id,
            "customer_id": customer["customer_id"],
            "account_type": random.choice(account_types),
            "balance": random.randint(5000, 1000000)
        })

        account_id += 1

df_accounts = pd.DataFrame(accounts)

df_accounts.to_csv(
    "../data/raw/accounts.csv",
    index=False
)

print(
    f"{len(df_accounts)} accounts generated successfully"
)