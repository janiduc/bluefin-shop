"""Sales reporting: summary for the dashboard and a CSV export."""
import csv
import io

from .data import ORDERS


def dashboard_summary():
    paid = [o for o in ORDERS if o["status"] == "paid"]
    return {"orders": len(paid), "revenue": sum(o["total"] for o in paid)}


def export_csv():
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(["order_id", "customer", "total", "status"])
    for o in ORDERS:
        writer.writerow([o["id"], o["customer"], o["total"], o["status"]])
    writer.writerow(["TOTAL", "", sum(o["total"] for o in ORDERS), ""])
    return out.getvalue()
