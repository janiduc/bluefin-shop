# Bluefin Shop (toy project)

A deliberately small, fictional e-commerce API. It exists to give the
[issue triage proof of concept](https://github.com/janiduc/issue-triage-poc) a real GitHub
repository with real issues to import, classify, assign and close.

It is not a real shop. All data is in memory and invented. It contains bugs on purpose; see
`KNOWN_BUGS.md`.

## Run it

```bash
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5050. Tests: `python -m unittest`.

## Modules

| Area | File | Endpoints |
|---|---|---|
| Authentication | `shop/auth.py` | `POST /api/register`, `/api/login`, `/api/reset-password` |
| Payments | `shop/payments.py` | `POST /api/checkout` |
| Reporting | `shop/reporting.py` | `GET /api/reports/summary`, `/api/reports/export.csv` |
| API and search | `shop/catalog.py` | `GET /api/products?q=`, `/api/orders?page=` |
| User interface | `static/index.html` | `GET /` |

## Seed issues

`issues/seed_issues.json` holds 12 issues written the way real reporters write: clear bug
reports, a vague one, a duplicate, a feature request, a question, one with personal data to
test redaction, and one with a prompt-injection attempt.

To create them in this repository on GitHub:

```bash
python scripts/file_issues.py --dry-run
```

Then set `GITHUB_TOKEN` (fine-grained token, *Issues: read and write*) and
`GITHUB_REPO=owner/bluefin-shop`, and run it without `--dry-run`.

## Connecting the triage desk

In the triage project's `.env`:

```
TRACKER=github
GITHUB_TOKEN=<the same token>
GITHUB_REPO=owner/bluefin-shop
```

Restart the triage desk, sign in as `lead`, and press "Import from GitHub Issues".
