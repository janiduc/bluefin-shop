"""Product catalogue: search and paged order listing."""
from .data import ORDERS, PRODUCTS


def search(term):
    return [p for p in PRODUCTS if term in p["name"] or term in p["tags"]]


def list_orders(page=1, per_page=2):
    start = page * per_page
    return ORDERS[start:start + per_page]
