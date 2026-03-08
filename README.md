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
