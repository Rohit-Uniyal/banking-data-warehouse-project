from load import get_connection
from logger import logger


def load_dim_customer():

    conn = None
    cursor = None

    try:

        logger.info("DIM_CUSTOMER Load Started")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            TRUNCATE TABLE warehouse.dim_customer
            RESTART IDENTITY
        """)

        cursor.execute("""
            INSERT INTO warehouse.dim_customer
            (
                customer_id,
                customer_name,
                city,
                annual_income
            )
            SELECT
                customer_id,
                customer_name,
                city,
                annual_income
            FROM staging.customer_test
        """)

        conn.commit()

        logger.info("DIM_CUSTOMER Loaded Successfully")
        print("DIM_CUSTOMER Loaded Successfully")

    except Exception as e:

        logger.error(f"DIM_CUSTOMER Failed : {e}")
        print(f"DIM_CUSTOMER Failed : {e}")

        if conn:
            conn.rollback()

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


def load_dim_account():

    conn = None
    cursor = None

    try:

        logger.info("DIM_ACCOUNT Load Started")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            TRUNCATE TABLE warehouse.dim_account
            RESTART IDENTITY
        """)

        cursor.execute("""
            INSERT INTO warehouse.dim_account
            (
                account_id,
                account_type
            )
            SELECT
                account_id,
                account_type
            FROM staging.account_test
        """)

        conn.commit()

        logger.info("DIM_ACCOUNT Loaded Successfully")
        print("DIM_ACCOUNT Loaded Successfully")

    except Exception as e:

        logger.error(f"DIM_ACCOUNT Failed : {e}")
        print(f"DIM_ACCOUNT Failed : {e}")

        if conn:
            conn.rollback()

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


def load_dim_date():

    conn = None
    cursor = None

    try:

        logger.info("DIM_DATE Load Started")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            TRUNCATE TABLE warehouse.dim_date
            RESTART IDENTITY
        """)

        cursor.execute("""
            INSERT INTO warehouse.dim_date
            (
                full_date,
                day_num,
                month_num,
                month_name,
                year_num
            )
            SELECT DISTINCT
                transaction_date,
                EXTRACT(DAY FROM transaction_date),
                EXTRACT(MONTH FROM transaction_date),
                TO_CHAR(transaction_date,'Month'),
                EXTRACT(YEAR FROM transaction_date)
            FROM staging.transaction_test
        """)

        conn.commit()

        logger.info("DIM_DATE Loaded Successfully")
        print("DIM_DATE Loaded Successfully")

    except Exception as e:

        logger.error(f"DIM_DATE Failed : {e}")
        print(f"DIM_DATE Failed : {e}")

        if conn:
            conn.rollback()

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()


def load_fact_transaction():

    conn = None
    cursor = None

    try:

        logger.info("FACT_TRANSACTION Load Started")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            TRUNCATE TABLE warehouse.fact_transaction
            RESTART IDENTITY
        """)

        cursor.execute("""
            INSERT INTO warehouse.fact_transaction
            (
                customer_key,
                account_key,
                date_key,
                transaction_id,
                amount,
                transaction_type
            )
            SELECT

                dc.customer_key,
                da.account_key,
                dd.date_key,

                t.transaction_id,
                t.amount,
                t.transaction_type

            FROM staging.transaction_test t

            JOIN staging.account_test a
                ON t.account_id = a.account_id

            JOIN warehouse.dim_customer dc
                ON a.customer_id = dc.customer_id

            JOIN warehouse.dim_account da
                ON a.account_id = da.account_id

            JOIN warehouse.dim_date dd
                ON t.transaction_date = dd.full_date
        """)

        conn.commit()

        logger.info("FACT_TRANSACTION Loaded Successfully")
        print("FACT_TRANSACTION Loaded Successfully")

    except Exception as e:

        logger.error(f"FACT_TRANSACTION Failed : {e}")
        print(f"FACT_TRANSACTION Failed : {e}")

        if conn:
            conn.rollback()

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()