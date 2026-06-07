from warehouse_loader import (
    load_dim_customer,
    load_dim_account,
    load_dim_date,
    load_fact_transaction
)

load_dim_customer()
load_dim_account()
load_dim_date()
load_fact_transaction()