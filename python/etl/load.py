import psycopg2
from psycopg2.extras import execute_values
from config import DB_CONFIG
from logger import logger


def get_connection():

    return psycopg2.connect(
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )


def load_customers(df):

    conn = None
    cursor = None

    try:

        logger.info("Customer Load Started")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "TRUNCATE TABLE staging.customer_test"
        )

        records = [
            (
                int(row["customer_id"]),
                row["customer_name"],
                row["city"],
                str(row["phone"]),
                float(row["annual_income"])
            )
            for _, row in df.iterrows()
        ]

        insert_query = """
        INSERT INTO staging.customer_test
        (
            customer_id,
            customer_name,
            city,
            phone,
            annual_income
        )
        VALUES %s
        """

        execute_values(
            cursor,
            insert_query,
            records
        )

        conn.commit()

        logger.info(
            f"{len(records)} customers loaded successfully"
        )

        print(
            f"{len(records)} customers loaded successfully"
        )

    except Exception as e:

        logger.error(
            f"Customer Load Failed : {e}"
        )

        print(
            f"Customer Load Failed : {e}"
        )

        if conn:
            conn.rollback()

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

        logger.info(
            "Customer Load Finished"
        )


def load_accounts(df):

    conn = None
    cursor = None

    try:

        logger.info("Account Load Started")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "TRUNCATE TABLE staging.account_test"
        )

        records = [
            (
                int(row["account_id"]),
                int(row["customer_id"]),
                row["account_type"],
                float(row["balance"])
            )
            for _, row in df.iterrows()
        ]

        insert_query = """
        INSERT INTO staging.account_test
        (
            account_id,
            customer_id,
            account_type,
            balance
        )
        VALUES %s
        """

        execute_values(
            cursor,
            insert_query,
            records
        )

        conn.commit()

        logger.info(
            f"{len(records)} accounts loaded successfully"
        )

        print(
            f"{len(records)} accounts loaded successfully"
        )

    except Exception as e:

        logger.error(
            f"Account Load Failed : {e}"
        )

        print(
            f"Account Load Failed : {e}"
        )

        if conn:
            conn.rollback()

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

        logger.info(
            "Account Load Finished"
        )


def load_transactions(df):

    conn = None
    cursor = None

    try:

        logger.info("Transaction Load Started")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "TRUNCATE TABLE staging.transaction_test"
        )

        records = [
            (
                int(row["transaction_id"]),
                int(row["account_id"]),
                row["transaction_type"],
                float(row["amount"]),
                row["transaction_date"]
            )
            for _, row in df.iterrows()
        ]

        insert_query = """
        INSERT INTO staging.transaction_test
        (
            transaction_id,
            account_id,
            transaction_type,
            amount,
            transaction_date
        )
        VALUES %s
        """

        execute_values(
            cursor,
            insert_query,
            records
        )

        conn.commit()

        logger.info(
            f"{len(records)} transactions loaded successfully"
        )

        print(
            f"{len(records)} transactions loaded successfully"
        )

    except Exception as e:

        logger.error(
            f"Transaction Load Failed : {e}"
        )

        print(
            f"Transaction Load Failed : {e}"
        )

        if conn:
            conn.rollback()

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()

        logger.info(
            "Transaction Load Finished"
        )