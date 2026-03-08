# Day 9 – Tuples and Sets

## Part A – Product Analytics Tool

### Overview

In this part of the assignment, we built a **Product Analytics Tool** using Python **tuples, namedtuples, and sets** to analyze customer shopping behavior in an e-commerce scenario.

The goal was to practice how tuples and sets can be used in real-world data processing tasks such as product catalog management, customer cart analysis, and product recommendations.

---

### Technologies Used

* Python
* Named Tuples (`collections.namedtuple`)
* Sets
* Set Operations (union, intersection, difference)

---

### Implementation Details

#### 1. Product Named Tuple

A `namedtuple` called **Product** was created with the following fields:

* `id`
* `name`
* `category`
* `price`

This allows products to behave like tuples while still having readable attribute names.

Example:

```python
from collections import namedtuple
Product = namedtuple("Product", ["id", "name", "category", "price"])
```

---

#### 2. Product Catalog

A catalog of **15 products** was created across **4 categories**:

* Electronics
* Clothing
* Books
* Home

Example product:

```python
Product(1, "Laptop", "Electronics", 75000)
```

---

#### 3. Customer Cart Sets

Five customer shopping carts were created using **sets of Product tuples**.

Example:

```python
customer_1_cart = {product1, product2, product5}
```

Using sets allows fast lookup and enables powerful set operations.

---

#### 4. Shopping Behaviour Analysis

Several analytics operations were performed:

**Bestsellers**

Products appearing in **all carts**.

```python
set.intersection(*all_carts)
```

**Catalog Reach**

Products appearing in **any cart**.

```python
set.union(*all_carts)
```

**Exclusive Purchases**

Products **only bought by customer 1**.

```python
customer_1_cart - other_carts
```

---

#### 5. Product Recommendation System

A function was implemented to suggest products that **other customers purchased but the current customer has not**.

Function:

```python
recommend_products(customer_cart, all_carts)
```

Logic used:

```
(all products bought by others) - (products already in cart)
```

---

#### 6. Category Summary

A function was created to group products by category.

Example output:

```python
{
 "Electronics": {"Laptop", "Smartphone"},
 "Books": {"Clean Code", "Python Crash Course"}
}
```

This helps in understanding catalog distribution.

---

### Key Concepts Practiced

* Tuple creation
* Named tuples
* Set creation
* Set intersection
* Set union
* Set difference
* Using sets for analytics
* Basic recommendation logic

---

### Learning Outcome

This exercise demonstrates how **Python tuples and sets can be used to efficiently model and analyze data in real-world applications like e-commerce systems.**
## Part B – Frozenset Bundle System

### Overview

In this part of the assignment, we explored **frozenset**, an immutable version of Python’s set.
The goal was to understand when frozensets are useful in real-world systems and implement a **bundle discount system** for an e-commerce platform.

---

### What is a Frozenset?

A **frozenset** is an immutable version of a Python set.

Once created, its elements **cannot be modified**, meaning you cannot add or remove items.

Example:

```python
bundle = frozenset({"Electronics", "Books"})
```

---

### Difference Between Set and Frozenset

| Feature                 | set | frozenset |
| ----------------------- | --- | --------- |
| Mutable                 | Yes | No        |
| Can add/remove elements | Yes | No        |
| Can be dictionary key   | No  | Yes       |

Since dictionary keys must be **immutable**, `frozenset` is useful when storing fixed groups of values.

---

### Bundle Discount System

A dictionary named **`bundle_discounts`** was created where:

* **Key** → `frozenset` of product categories
* **Value** → discount percentage

Example:

```python
bundle_discounts = {
 frozenset({"Electronics", "Books"}): 10
}
```

This means if a customer buys items from **Electronics and Books**, they receive a **10% discount**.

---

### Bundle Checker Function

A function called **`check_bundle_discount(cart)`** was implemented.

Purpose:

* Extract product categories from the cart
* Check if the cart qualifies for any bundle discount

Example logic:

```python
categories = {product.category for product in cart}
```

If a matching bundle is found, the corresponding **discount percentage** is returned.

---

### Performance Benchmark

To compare performance, the creation time of `set` and `frozenset` was measured using the **timeit module**.

Test configuration:

* **100000 iterations**

Example code:

```python
timeit.timeit("set([1,2,3,4])", number=100000)
```

Observation:

* The creation time of `set` and `frozenset` is **very similar**.
* The main difference is **immutability**, not performance.

---

### Key Concepts Practiced

* Frozenset creation
* Immutable data structures
* Using frozenset as dictionary keys
* Bundle logic implementation
* Performance benchmarking with `timeit`

---

### Learning Outcome

This exercise demonstrates how immutable data structures like **frozenset** are useful when storing **fixed combinations of values**, such as bundle deals, permissions, or configuration groups in real-world systems.

