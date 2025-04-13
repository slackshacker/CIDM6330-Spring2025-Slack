# D:\cidm6330\ppm\tasks.py

from celery import shared_task
import time

@shared_task
def simulate_long_task(name, seconds):
    time.sleep(seconds)
    return f"{name} task completed after {seconds} seconds."