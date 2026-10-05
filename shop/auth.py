"""Accounts: register, log in, reset password."""
import hashlib

from .data import USERS


def _hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password):
    if username in USERS:
        raise ValueError("Username already taken")
    USERS[username] = _hash(password)


def login(username, password):
    return USERS.get(username) == _hash(password)


def reset_password(username, new_password):
    if username not in USERS:
        raise ValueError("Unknown user")
    USERS[username] = _hash(new_password.strip().lower())
