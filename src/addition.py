# app.py
# This is a test commit

def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0


# GitHub Actions → Docker Hub/GHCR → SSH to Droplet → docker compose pull && docker compose up -d.
