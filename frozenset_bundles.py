"""
PART B — Frozenset Bundles

What is frozenset?
A frozenset is an immutable version of a set in Python.
Once created, its elements cannot be changed (no add/remove).

Difference between set and frozenset

set
- Mutable
- Elements can be added or removed
- Cannot be used as dictionary keys

frozenset
- Immutable
- Elements cannot be modified
- Can be used as dictionary keys

Real-world usage
frozenset is useful when we want fixed collections that should not change,
such as bundle deals, permission groups, or configuration sets.
"""

import timeit
from collections import namedtuple


# Product structure (same as Part A)
Product = namedtuple("Product", ["id", "name", "category", "price"])


# Sample products (for testing bundle system)
p1 = Product(1, "Laptop", "Electronics", 75000)
p2 = Product(2, "Clean Code", "Books", 600)
p3 = Product(3, "Jeans", "Clothing", 2000)
p4 = Product(4, "Blender", "Home", 3000)


# Example customer cart
cart = {p1, p2}


# Bundle Discount Dictionary
# Keys are frozensets of categories
# Values are discount percentages

bundle_discounts = {
    frozenset({"Electronics", "Books"}): 10,
    frozenset({"Clothing", "Home"}): 15,
    frozenset({"Electronics", "Clothing"}): 5
}


# Bundle Checker Function

def check_bundle_discount(cart):

    # Extract categories from cart
    categories = {product.category for product in cart}

    # Check if any bundle condition matches
    for bundle, discount in bundle_discounts.items():

        if bundle.issubset(categories):
            return discount

    return 0


# Test bundle discount system
discount = check_bundle_discount(cart)

print("Cart Categories:", {p.category for p in cart})
print("Applicable Discount:", discount, "%")


# Performance Benchmark

set_time = timeit.timeit(
    stmt="set([1,2,3,4])",
    number=100000
)

frozenset_time = timeit.timeit(
    stmt="frozenset([1,2,3,4])",
    number=100000
)


print("\nPerformance Benchmark (100000 iterations)")
print("Set creation time:", set_time)
print("Frozenset creation time:", frozenset_time)