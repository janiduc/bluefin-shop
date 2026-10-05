"""Bluefin Shop: a deliberately small e-commerce API used as a test target for issue triage."""
from flask import Flask, Response, jsonify, request, send_from_directory

from . import auth, catalog, payments, reporting
from .data import STORE


def create_app():
    app = Flask(__name__, static_folder="../static")

    @app.errorhandler(ValueError)
    def bad_request(exc):
        return jsonify(error=str(exc)), 400

    @app.get("/")
    def index():
        return send_from_directory(app.static_folder, "index.html")

    @app.get("/api/store")
    def store():
        return jsonify(STORE)

    @app.post("/api/register")
    def register():
        data = request.get_json(force=True)
        auth.register(data["username"], data["password"])
        return jsonify(ok=True), 201

    @app.post("/api/login")
    def login():
        data = request.get_json(force=True)
        if not auth.login(data["username"], data["password"]):
            return jsonify(error="Invalid credentials"), 401
        return jsonify(ok=True)

    @app.post("/api/reset-password")
    def reset_password():
        data = request.get_json(force=True)
        auth.reset_password(data["username"], data["new_password"])
        return jsonify(ok=True)

    @app.get("/api/products")
    def products():
        return jsonify(catalog.search(request.args.get("q", "")))

    @app.get("/api/orders")
    def orders():
        return jsonify(catalog.list_orders(int(request.args.get("page", 1))))

    @app.post("/api/checkout")
    def checkout():
        data = request.get_json(force=True)
        order = payments.checkout(data["customer"], data["product_ids"], data.get("code"))
        return jsonify(order), 201

    @app.get("/api/reports/summary")
    def summary():
        return jsonify(reporting.dashboard_summary())

    @app.get("/api/reports/export.csv")
    def export():
        return Response(reporting.export_csv(), mimetype="text/csv")

    return app
