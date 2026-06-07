import pandas as pd


def extract_customers():

    df = pd.read_csv(
        "../../data/raw/customers.csv"
    )

    print(
        f"Customers Extracted: {len(df)}"
    )

    return df


def extract_accounts():

    df = pd.read_csv(
        "../../data/raw/accounts.csv"
    )

    print(
        f"Accounts Extracted: {len(df)}"
    )

    return df


def extract_transactions():

    df = pd.read_csv(
        "../../data/raw/transactions.csv"
    )

    print(
        f"Transactions Extracted: {len(df)}"
    )

    return df


if __name__ == "__main__":

    extract_customers()

    extract_accounts()

    extract_transactions()