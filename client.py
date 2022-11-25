import json
import requests
import pandas as pd

df = pd.read_csv("/home/alvynabranches/Downloads/accepted_2007_to_2018Q4.csv")
data = df.to_dict("records")
for d in data:
    res = requests.post("http://localhost:5000/transaction", data=json.dumps(d))
    print(res)