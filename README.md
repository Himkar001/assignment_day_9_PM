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

## Part C – Interview Ready Questions

### Overview

This section focuses on **common Python interview concepts** related to tuples and sets.
It includes conceptual explanations, coding exercises, and debugging tasks that test understanding of Python data structures.

---

### Q1 – Tuple Immutability Trap

Consider the tuple:

```python
t = ([1,2], [3,4])
```

Can we execute:

```python
t[0][0] = 99
```

#### Answer

Yes, this operation works.

Even though **tuples are immutable**, the objects stored inside them may still be **mutable**.

In this example:

* The tuple contains **lists**
* Lists are **mutable objects**

Therefore, modifying an element inside the list is allowed.

Example result:

```python
([99,2], [3,4])
```

However, this would fail:

```python
t[0] = [9,9]
```

because tuple elements themselves **cannot be reassigned**.

---

### Q2 – Duplicate Detection Using Sets

A function was implemented to find duplicate elements in a list using set operations.

Example implementation:

```python
def find_duplicates(lst):

    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates
```

Example usage:

```python
find_duplicates([1,2,3,2,4,5,1])
```

Output:

```
{1, 2}
```

Time Complexity: **O(n)**

---

### Q3 – Debugging Problem

Original buggy function:

```python
def unique_to_each(a, b):
    result = set(a) - set(b)
    return list(result)
```

#### Issue

This function only returns elements unique to **list A**, not both lists.

Example:

```python
unique_to_each([1,2,3], [3,4,5])
```

Output:

```
[1,2]
```

Expected result:

```
[1,2,4,5]
```

#### Correct Implementation

```python
def unique_to_each(a, b):

    set_a = set(a)
    set_b = set(b)

    return list((set_a - set_b) | (set_b - set_a))
```

#### Explanation

* `set_a - set_b` → elements only in list A
* `set_b - set_a` → elements only in list B
* `|` → union of both results

This returns elements unique to each list.

---

### Key Concepts Covered

* Tuple immutability
* Mutable vs immutable objects
* Set operations
* Efficient duplicate detection
* Debugging Python functions
* Interview-style Python questions

---

### Learning Outcome

This section demonstrates how Python tuples and sets behave in practical scenarios and highlights important concepts frequently tested in **technical interviews and coding assessments**.

## Part D – AI Augmented Task (Jaccard Similarity)

### Overview

In this section, an AI tool was used to generate a Python function that calculates **Jaccard Similarity** between two sets of strings. The task involved evaluating the AI-generated solution, testing it with sample data, and researching where this metric is used in real-world applications.

---

### What is Jaccard Similarity?

Jaccard similarity is a metric used to measure the similarity between two sets.

Formula:

```
J(A,B) = |A ∩ B| / |A ∪ B|
```

Where:

* **A ∩ B** → Intersection of the two sets
* **A ∪ B** → Union of the two sets

The value ranges between **0 and 1**:

* **0** → No common elements
* **1** → Identical sets

---

### Python Implementation

```python id="1ah1wh"
def jaccard_similarity(set_a, set_b):

    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)

    if len(union) == 0:
        return 0

    return len(intersection) / len(union)
```

---

### Test Example

```python id="p3f7vf"
set_a = {'python','java','sql'}
set_b = {'python','sql','docker','aws'}

print(jaccard_similarity(set_a,set_b))
```

Output:

```
0.5
```

Explanation:

Intersection = `{'python','sql'}` → size = 2
Union = `{'python','java','sql','docker','aws'}` → size = 4

Jaccard Similarity = **2 / 4 = 0.5**

---

### Edge Case Handling

The implementation includes a condition to handle cases where both sets are empty.

```python id="z91rsk"
if len(union) == 0:
    return 0
```

This prevents division-by-zero errors.

---

### Industry Applications

Jaccard similarity is widely used in several industry applications:

* **Recommendation Systems** – comparing user interests or purchase history
* **Natural Language Processing (NLP)** – measuring similarity between documents
* **Plagiarism Detection** – identifying overlapping text between documents
* **Search Engines** – ranking results based on similarity between queries and documents

---

### Learning Outcome

This exercise demonstrates how AI tools can assist in generating code solutions and how developers must evaluate correctness, handle edge cases, and understand practical industry applications.

