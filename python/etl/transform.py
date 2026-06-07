def transform_customers(df):

    original_count = len(df)

    df = df.drop_duplicates()

    df = df.dropna()

    print(f"Customer Records Before : {original_count}")
    print(f"Customer Records After  : {len(df)}")

    return df


def transform_accounts(df):

    original_count = len(df)

    df = df.drop_duplicates()

    df = df.dropna()

    print(f"Account Records Before : {original_count}")
    print(f"Account Records After  : {len(df)}")

    return df


def transform_transactions(df):

    original_count = len(df)

    df = df.drop_duplicates()

    df = df.dropna()

    print(f"Transaction Records Before : {original_count}")
    print(f"Transaction Records After  : {len(df)}")

    return df