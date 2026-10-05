"""In-memory demo data. Everything here is fictional."""
from datetime import date

STORE = {"name": "Bluefin Shop", "currency": "LKR"}

PRODUCTS = [
    {"id": 1, "name": "Running Shoes", "price": 12500.0, "tags": ["shoes", "sport"]},
    {"id": 2, "name": "Leather Wallet", "price": 4200.0, "tags": ["accessories"]},
    {"id": 3, "name": "Canvas Backpack", "price": 7800.0, "tags": ["bags", "travel"]},
    {"id": 4, "name": "Steel Water Bottle", "price": 1900.0, "tags": ["sport", "travel"]},
    {"id": 5, "name": "Wool Scarf", "price": 3100.0, "tags": ["accessories", "winter"]},
]

DISCOUNT_CODES = {
    "WELCOME10": {"percent": 10, "expires": date(2099, 12, 31)},
    "SUMMER25": {"percent": 25, "expires": date(2025, 8, 31)},
    "LOYAL15": {"percent": 15, "expires": None},  # never expires
}

# username -> password hash (see auth.py)
USERS = {}

ORDERS = [
    {"id": 101, "customer": "amal", "total": 12500.0, "status": "paid"},
    {"id": 102, "customer": "nimal", "total": 4200.0, "status": "refunded"},
    {"id": 103, "customer": "kamal", "total": 7800.0, "status": "paid"},
    {"id": 104, "customer": "sunil", "total": 1900.0, "status": "paid"},
    {"id": 105, "customer": "amal", "total": 3100.0, "status": "refunded"},
    {"id": 106, "customer": "ruwan", "total": 9700.0, "status": "paid"},
]
