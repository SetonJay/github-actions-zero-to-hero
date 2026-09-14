import time
import os
import requests

start_time = time.time()
end_time = time.time()
start_url = 'https://bullcarpwebsite.local/server/auth'
aws_access = 'info8372t8273tr(*56342214&$&&T&nwodnornfo38'
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC7FAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKE
FAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKE
-----END RSA PRIVATE KEY-----
"""

def add(a: any, b: any):
    ''' function-docstring: Basic add function '''
    result = a + b
    return result

def test_add():
    ''' function-docstring: Basic test for add fuction'''
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(3, -1) == 0
print(
        f"\nExecution Time: {end_time - start_time} seconds to {start_url} with key {aws_access} "
        )


# PR Merged --> Checkout --> Gitleaks (Secrets scan) --> CodeQL (SAST) --> Trivy FS (Dependencies) --> Docker Build --> Trivy Image Scan --> Push to GHCR
# GitHub Actions → Docker Hub/GHCR → SSH to Droplet → docker compose pull && docker compose up -d.
