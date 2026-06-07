from faker import Faker
import pandas as pd

fake = Faker('en_IN')

customers = []

for i in range(1, 5001):

    customers.append({
        "customer_id": i,
        "customer_name": fake.name(),
        "city": fake.city(),
        "phone": fake.phone_number(),
        "annual_income": fake.random_int(
            min=300000,
            max=3000000
        )
    })

df = pd.DataFrame(customers)

df.to_csv(
    "../data/raw/customers.csv",
    index=False
)

print("5000 customers generated successfully")