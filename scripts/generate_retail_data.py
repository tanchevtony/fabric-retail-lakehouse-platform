import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random
import os

fake = Faker("en_GB")

random.seed(42)
np.random.seed(42)

# ====================================================
# CONFIG
# ====================================================

N_CUSTOMERS = 100_000
N_PRODUCTS = 5_000
N_STORES = 100
N_ORDERS = 500_000
N_RETURNS = 25_000

OUTPUT_DIR = "datasets/raw"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ====================================================
# CUSTOMERS
# ====================================================

print("Generating customers...")

customers = []

loyalty_tiers = ["Bronze", "Silver", "Gold"]
tier_weights = [0.65, 0.25, 0.10]

for i in range(1, N_CUSTOMERS + 1):
    signup_date = fake.date_between(
        start_date="-4y",
        end_date="today"
    )

    customers.append({
        "customer_id": f"C{i:06}",
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "city": fake.city(),
        "country": "United Kingdom",
        "signup_date": signup_date,
        "loyalty_tier": np.random.choice(
            loyalty_tiers,
            p=tier_weights
        )
    })

customers_df = pd.DataFrame(customers)

# introduce bad data

mask = np.random.choice(
    customers_df.index,
    size=int(len(customers_df) * 0.02),
    replace=False
)

customers_df.loc[mask, "email"] = None

customers_df.to_csv(
    f"{OUTPUT_DIR}/customers.csv",
    index=False
)

print("Customers complete")

# ====================================================
# PRODUCTS
# ====================================================

print("Generating products...")

categories = {
    "Electronics": ["Samsung", "Apple", "Sony"],
    "Fashion": ["Nike", "Adidas", "Puma"],
    "Home": ["Ikea", "Philips", "Bosch"],
    "Sports": ["Wilson", "Under Armour", "Reebok"],
    "Books": ["Penguin", "HarperCollins"]
}

products = []

for i in range(1, N_PRODUCTS + 1):

    category = random.choice(list(categories.keys()))
    brand = random.choice(categories[category])

    cost_price = round(
        random.uniform(5, 500),
        2
    )

    selling_price = round(
        cost_price * random.uniform(1.2, 2.0),
        2
    )

    products.append({
        "product_id": f"P{i:05}",
        "product_name": f"{brand} Product {i}",
        "category": category,
        "brand": brand,
        "cost_price": cost_price,
        "selling_price": selling_price,
        "launch_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })

products_df = pd.DataFrame(products)

products_df.to_csv(
    f"{OUTPUT_DIR}/products.csv",
    index=False
)

print("Products complete")

# ====================================================
# STORES
# ====================================================

print("Generating stores...")

cities = [
    "London",
    "Manchester",
    "Birmingham",
    "Leeds",
    "Liverpool",
    "Bristol",
    "Glasgow",
    "Cardiff"
]

stores = []

for i in range(1, N_STORES + 1):

    city = random.choice(cities)

    stores.append({
        "store_id": f"S{i:03}",
        "store_name": f"{city} Store {i}",
        "city": city,
        "country": "United Kingdom",
        "open_date": fake.date_between(
            start_date="-10y",
            end_date="-1y"
        )
    })

stores_df = pd.DataFrame(stores)

stores_df.to_csv(
    f"{OUTPUT_DIR}/stores.csv",
    index=False
)

print("Stores complete")

# ====================================================
# ORDERS
# ====================================================

print("Generating orders...")

customer_ids = customers_df["customer_id"].tolist()
store_ids = stores_df["store_id"].tolist()

orders = []

for i in range(1, N_ORDERS + 1):

    order_date = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    sales_channel = np.random.choice(
        ["Store", "Online"],
        p=[0.6, 0.4]
    )

    orders.append({
        "order_id": f"O{i:08}",
        "customer_id": random.choice(customer_ids),
        "store_id": random.choice(store_ids),
        "order_date": order_date,
        "sales_channel": sales_channel,
        "payment_method": random.choice(
            [
                "Card",
                "Cash",
                "PayPal",
                "Apple Pay"
            ]
        ),
        "total_amount": round(
            random.uniform(10, 1500),
            2
        )
    })

orders_df = pd.DataFrame(orders)

# future dates (bad data)

bad_dates = np.random.choice(
    orders_df.index,
    size=500,
    replace=False
)

orders_df.loc[
    bad_dates,
    "order_date"
] = "2099-01-01"

orders_df.to_csv(
    f"{OUTPUT_DIR}/orders.csv",
    index=False
)

print("Orders complete")

# ====================================================
# ORDER ITEMS
# ====================================================

print("Generating order items...")

product_ids = products_df["product_id"].tolist()

items = []
item_counter = 1

sample_orders = orders_df.sample(
    min(200000, len(orders_df))
)

for _, order in sample_orders.iterrows():

    item_count = random.randint(1, 5)

    for _ in range(item_count):

        quantity = random.randint(1, 5)

        product = random.choice(product_ids)

        unit_price = float(
            products_df.loc[
                products_df["product_id"] == product,
                "selling_price"
            ].iloc[0]
        )

        items.append({
            "order_item_id": f"OI{item_counter:09}",
            "order_id": order["order_id"],
            "product_id": product,
            "quantity": quantity,
            "unit_price": unit_price,
            "discount_amount": round(
                random.uniform(0, 20),
                2
            )
        })

        item_counter += 1

order_items_df = pd.DataFrame(items)

order_items_df.to_csv(
    f"{OUTPUT_DIR}/order_items.csv",
    index=False
)

print("Order Items complete")

# ====================================================
# RETURNS
# ====================================================

print("Generating returns...")

returns = []

return_reasons = [
    "Damaged Product",
    "Wrong Item",
    "Customer Changed Mind",
    "Late Delivery"
]

sample_return_orders = orders_df.sample(
    N_RETURNS
)

for i, (_, order) in enumerate(
    sample_return_orders.iterrows(),
    start=1
):

    returns.append({
        "return_id": f"R{i:07}",
        "order_id": order["order_id"],
        "return_date": fake.date_between(
            start_date="-1y",
            end_date="today"
        ),
        "return_reason": random.choice(
            return_reasons
        ),
        "refund_amount": round(
            random.uniform(10, 500),
            2
        )
    })

returns_df = pd.DataFrame(returns)

returns_df.to_csv(
    f"{OUTPUT_DIR}/returns.csv",
    index=False
)

print("Returns complete")

# ====================================================
# SUMMARY
# ====================================================

print("\nDataset Summary")
print("------------------------------")
print("Customers:", len(customers_df))
print("Products:", len(products_df))
print("Stores:", len(stores_df))
print("Orders:", len(orders_df))
print("Order Items:", len(order_items_df))
print("Returns:", len(returns_df))
print("------------------------------")