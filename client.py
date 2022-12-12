import json
import requests
import pandas as pd
from time import perf_counter

host = "34.123.210.194"
path = "."
df = pd.read_csv(f"{path}/rejected_2007_to_2018Q4.csv")
print(f"Done Loading Document with {len(df)} records.", end="\r")
data = df.to_dict("records")
for d in data:
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
    print(json.dumps(d, indent=4))
    print(json.dumps(data, indent=4))
    input("Waiting!!!")
    s = perf_counter()
    res = requests.post(f"http://{host}/transaction", data=json.dumps(data))
    e = perf_counter()
    print(f"Time Taken: {e-s:.2f} seconds")
    print(res)
