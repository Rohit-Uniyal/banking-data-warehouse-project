from extract import (
    extract_customers,
    extract_accounts,
    extract_transactions
)

from transform import (
    transform_customers,
    transform_accounts,
    transform_transactions
)

customers = transform_customers(
    extract_customers()
)

accounts = transform_accounts(
    extract_accounts()
)

transactions = transform_transactions(
    extract_transactions()
)