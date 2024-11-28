import requests
import random
import time

vip = "10.0.0.2"  # Virtual IP for the load balancer
port = 80

while True:
    try:
        response = requests.get(f"http://{vip}:{port}")
        print(f"Response from {vip}: {response.status_code}")
    except Exception as e:
        print(f"Failed to connect to {vip}: {e}")

    time.sleep(random.uniform(0.5, 2))