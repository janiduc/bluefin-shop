"""Happy-path tests. They pass, and deliberately do not cover the known bugs (see KNOWN_BUGS.md)."""
import unittest

from shop import create_app
from shop.data import ORDERS, USERS


class ShopTests(unittest.TestCase):
    def setUp(self):
        USERS.clear()
        del ORDERS[6:]  # drop orders created by earlier tests
        self.client = create_app().test_client()

    def test_register_and_login(self):
        self.client.post("/api/register", json={"username": "amal", "password": "secret123"})
        res = self.client.post("/api/login", json={"username": "amal", "password": "secret123"})
        self.assertEqual(res.status_code, 200)

    def test_checkout_with_valid_code(self):
        res = self.client.post("/api/checkout", json={
            "customer": "amal", "product_ids": [2], "code": "WELCOME10"})
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.get_json()["total"], 3780.0)

    def test_expired_code_rejected(self):
        res = self.client.post("/api/checkout", json={
            "customer": "amal", "product_ids": [2], "code": "SUMMER25"})
        self.assertEqual(res.status_code, 400)

    def test_search_by_exact_name(self):
        res = self.client.get("/api/products?q=Wallet")
        self.assertEqual([p["id"] for p in res.get_json()], [2])

    def test_dashboard_excludes_refunds(self):
        summary = self.client.get("/api/reports/summary").get_json()
        self.assertEqual(summary["orders"], 4)


if __name__ == "__main__":
    unittest.main()
