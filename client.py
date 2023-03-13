import os
import json
import requests
import pandas as pd
from time import perf_counter

host = "34.123.210.194"
folder = os.path.join(os.path.dirname(__file__), "data")
files = [os.path.join(folder, file) for file in os.listdir(folder)]
for file in files:
    data = json.load(open(file))
    print(data)
    input("Waiting!!!")
    s = perf_counter()
    res = requests.post(f"http://{host}/transaction", data=json.dumps(data))
    e = perf_counter()
    print(f"Time Taken: {e-s:.2f} seconds")
    print(res)
