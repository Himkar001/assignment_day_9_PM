"""
Product Analytics Tool
Using tuples and sets to analyze shopping behaviour
"""

from collections import namedtuple

# 1️⃣ Define Named Tuple
Product = namedtuple("Product", ["id", "name", "category", "price"])


# 2️⃣ Product Catalog (15 products, 4 categories)

catalog = [
    Product(1, "Laptop", "Electronics", 75000),
    Product(2, "Smartphone", "Electronics", 50000),
    Product(3, "Headphones", "Electronics", 5000),
    Product(4, "Smartwatch", "Electronics", 12000),

    Product(5, "Tshirt", "Clothing", 800),
    Product(6, "Jeans", "Clothing", 2000),
    Product(7, "Jacket", "Clothing", 3500),
    Product(8, "Sneakers", "Clothing", 4000),

    Product(9, "Clean Code", "Books", 600),
    Product(10, "Python Crash Course", "Books", 700),
    Product(11, "Deep Learning", "Books", 900),

    Product(12, "Blender", "Home", 3000),
    Product(13, "Coffee Maker", "Home", 4500),
    Product(14, "Vacuum Cleaner", "Home", 7000),
    Product(15, "Air Fryer", "Home", 6500),
]


# 3️⃣ Customer Cart Sets

customer_1_cart = {catalog[0], catalog[4], catalog[8], catalog[12]}
customer_2_cart = {catalog[1], catalog[4], catalog[9], catalog[12]}
customer_3_cart = {catalog[0], catalog[6], catalog[8], catalog[13]}
customer_4_cart = {catalog[2], catalog[4], catalog[10], catalog[12]}
customer_5_cart = {catalog[0], catalog[5], catalog[8], catalog[12]}

all_carts = [
    customer_1_cart,
    customer_2_cart,
    customer_3_cart,
    customer_4_cart,
    customer_5_cart
]


# 4️⃣ Analyze Shopping Behaviour

# (a) Bestsellers (products appearing in ALL carts)
bestsellers = set.intersection(*all_carts)

# (b) Catalog Reach (products appearing in ANY cart)
catalog_reach = set.union(*all_carts)

# (c) Exclusive Purchases (only customer 1 bought)
other_carts = set.union(*all_carts[1:])
exclusive_customer1 = customer_1_cart - other_carts


# 5️⃣ Product Recommendation Function

def recommend_products(customer_cart, all_carts):
    """
    Suggest products other customers bought but this customer didn't
    """
    all_products = set.union(*all_carts)
    recommendations = all_products - customer_cart
    return recommendations


# 6️⃣ Category Summary

def category_summary():
    """
    Returns products grouped by category
    """
    summary = {}

    for product in catalog:
        summary.setdefault(product.category, set()).add(product.name)

    return summary


# Run Demo

if __name__ == "__main__":

    print("\nBestsellers (products in ALL carts):")
    print(bestsellers)

    print("\nCatalog Reach (products in ANY cart):")
    print(catalog_reach)

    print("\nExclusive Purchases (only customer 1 bought):")
    print(exclusive_customer1)

    print("\nRecommended Products for Customer 1:")
    print(recommend_products(customer_1_cart, all_carts))

    print("\nCategory Summary:")
    print(category_summary())