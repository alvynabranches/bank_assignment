import json
import requests
import pandas as pd
from time import perf_counter

host = "104.197.157.84"
port = 5000
path = "."
df = pd.read_csv(f"{path}/rejected_2007_to_2018Q4.csv")
print(f"Done Loading Document with {len(df)} records.", end="\r")
data = df.to_dict("records")
for d in data:
    print(d)
    input("Waiting!!!")
    data = {}
    data["amount_requested"] = d["Amount Requested"]
    data["application_date"] = d["Application Date"]
    data["loan_title"] = d["Loan Title"]
    data["risk_score"] = d["Risk_Score"]
    data["debt_to_income_ratio"] = d["Debt-To-Income Ratio"]
    data["zip_code"] = d["Zip Code"]
    data["state"] = d["State"]
    data["employment_length"] = d["Employment Length"]
    data["policy_code"] = d["Policy Code"]
    print(data, end="\r")
    s = perf_counter()
    res = requests.post(f"http://{host}:{port}/transaction", data=json.dumps(data))
    e = perf_counter()
    print(f"Time Taken: {e-s:.2f} seconds")
    print(res)
