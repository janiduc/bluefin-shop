"""Checkout: price a basket, apply a discount code, record the order."""
from datetime import date

from .data import DISCOUNT_CODES, ORDERS, PRODUCTS


def apply_discount(subtotal, code):
    discount = DISCOUNT_CODES.get(code.upper())
    if not discount:
        raise ValueError("Unknown discount code")
    if discount["expires"] < date.today():
        raise ValueError("Discount code has expired")
    return round(subtotal * (100 - discount["percent"]) / 100, 2)


def checkout(customer, product_ids, code=None):
    prices = {p["id"]: p["price"] for p in PRODUCTS}
    unknown = [i for i in product_ids if i not in prices]
    if unknown or not product_ids:
        raise ValueError("Basket is empty or contains unknown products")
    total = sum(prices[i] for i in product_ids)
    if code:
        total = apply_discount(total, code)
    order = {"id": max(o["id"] for o in ORDERS) + 1, "customer": customer,
             "total": total, "status": "paid"}
    ORDERS.append(order)
    return order
