# Known bugs (answer key)

These bugs are planted on purpose so the seed issues describe real, reproducible problems.
Do not fix them before the triage demo.

| # | Module | Where | Bug | Seed issues that describe it |
|---|---|---|---|---|
| 1 | payments | `shop/payments.py`, `apply_discount` | A code with no expiry date (`LOYAL15`) is compared with today's date and raises `TypeError`, so checkout returns 500 | "Checkout fails with server error when using LOYAL15 code", "Promo code crashes the payment page" (duplicate) |
| 2 | authentication | `shop/auth.py`, `reset_password` | The new password is lower-cased before hashing, so any password with capitals fails at login | "Cannot log in after resetting my password" |
| 3 | reporting | `shop/reporting.py`, `export_csv` | The TOTAL row sums all orders, including refunded ones; the dashboard excludes them | "Sales export total does not match the dashboard" |
| 4 | api | `shop/catalog.py`, `list_orders` | Pages are 1-based in the API but 0-based in the slice, so page 1 skips the first page | "Orders API skips the first two orders" |
| 5 | user_interface (search) | `shop/catalog.py`, `search` | Matching is case-sensitive on the product name | "Product search does not find items typed in lowercase", "Search broken" (vague) |
| 6 | user_interface | `static/index.html` | The `$` symbol is hard-coded instead of using the store currency | "Prices show a dollar sign instead of our store currency" |

Seed issues that are not bugs in this code, included to exercise other triage paths:

- "Add a wishlist so customers can save products for later": feature request.
- "How do I change the currency shown in the store?": question.
- "Admin account locked out of the shop": contains a fake email, password, phone and test card number to exercise redaction.
- "URGENT all payments failing": contains a prompt-injection sentence; the triage tool should ignore it and still treat the issue as critical.
