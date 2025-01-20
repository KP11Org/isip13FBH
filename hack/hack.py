import requests
import time

while True:
    time.sleep(10)
    data = requests.get("https://67877325c4a42c916106c0c3.mockapi.io/task")
    for item in data.json():
        id = item["id"]
        requests.delete(f"https://67877325c4a42c916106c0c3.mockapi.io/task/{id}")
        print(f"Deleted item {id}")
        time.sleep(2)
