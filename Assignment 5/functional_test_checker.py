import subprocess
import requests
import time
import os
import sys
from django.core.management import call_command
from importlib import import_module

# Ensure Django environment is set up
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CIDM6330.settings")
import django
django.setup()

def check_django_server():
    print("[1] Checking Django server root URL...")
    try:
        r = requests.get("http://127.0.0.1:8000/")
        assert r.status_code == 200
        print("Django server responded OK.")
    except Exception as e:
        print("Failed to connect to Django root URL:", e)

def check_api_endpoint():
    print("[2] Checking DRF /api/applicants/ endpoint...")
    try:
        r = requests.get("http://127.0.0.1:8000/api/applicants/")
        assert r.status_code == 200
        print("API endpoint is working.")
    except Exception as e:
        print("Failed to connect to API endpoint:", e)

def check_redis():
    print("[3] Checking Redis availability...")
    try:
        out = subprocess.check_output(["redis-cli", "ping"]).decode().strip()
        assert out == "PONG"
        print("Redis is running.")
    except Exception as e:
        print("Redis check failed:", e)

def check_celery_task():
    print("[4] Testing Celery task...")
    try:
        tasks = import_module("api.tasks")
        result = tasks.add.delay(10, 15)
        print("   Waiting for result...")
        time.sleep(2)
        assert result.get(timeout=10) == 25
        print("Celery task executed successfully.")
    except Exception as e:
        print("Celery task failed:", e)

def check_admin_access():
    print("[5] Checking /admin/ page access...")
    try:
        r = requests.get("http://127.0.0.1:8000/admin/")
        assert r.status_code == 200
        print("Admin page is reachable (login required).")
    except Exception as e:
        print("Admin page not reachable:", e)

def run_unit_tests():
    print("[6] Running Django unit tests...")
    try:
        call_command("test", verbosity=1)
        print("Unit tests executed.")
    except Exception as e:
        print("Unit test run failed:", e)

if __name__ == "__main__":
    print("\n--- FUNCTIONAL CHECKS FOR CIDM6330 PROJECT ---\n")
    check_django_server()
    check_api_endpoint()
    check_redis()
    check_celery_task()
    check_admin_access()
    run_unit_tests()
    print("\n--- CHECK COMPLETE ---\n")
