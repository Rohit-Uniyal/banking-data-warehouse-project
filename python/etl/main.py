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

from load import (
    load_customers,
    load_accounts,
    load_transactions
)

from logger import logger


def main():

    try:

        logger.info("ETL Started")

        # Customers
        customers_df = extract_customers()

        customers_df = transform_customers(
            customers_df
        )

        load_customers(
            customers_df
        )

        # Accounts
        accounts_df = extract_accounts()

        accounts_df = transform_accounts(
            accounts_df
        )

        load_accounts(
            accounts_df
        )

        # Transactions
        transactions_df = extract_transactions()

        transactions_df = transform_transactions(
            transactions_df
        )

        load_transactions(
            transactions_df
        )

        logger.info("ETL Completed Successfully")

        print(
            "\nETL Completed Successfully"
        )

    except Exception as e:

        logger.error(
            f"ETL Failed : {e}"
        )

        print(
            f"\nETL Failed : {e}"
        )

    finally:

        logger.info(
            "ETL Process Finished"
        )


if __name__ == "__main__":
    main()