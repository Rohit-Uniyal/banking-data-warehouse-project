from warehouse_loader import (
    load_dim_customer,
    load_dim_account,
    load_dim_date,
    load_fact_transaction
)

from logger import logger


def main():

    try:

        logger.info(
            "WAREHOUSE ETL Started"
        )

        load_dim_customer()

        load_dim_account()

        load_dim_date()

        load_fact_transaction()

        logger.info(
            "WAREHOUSE ETL Completed Successfully"
        )

        print(
            "\nWAREHOUSE ETL Completed Successfully"
        )

    except Exception as e:

        logger.error(
            f"WAREHOUSE ETL Failed : {e}"
        )

        print(
            f"\nWAREHOUSE ETL Failed : {e}"
        )

    finally:

        logger.info(
            "WAREHOUSE ETL Finished"
        )


if __name__ == "__main__":
    main()