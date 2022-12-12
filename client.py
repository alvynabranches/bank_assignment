import json
import requests
import pandas as pd

host = "localhost"
path = "."
df = pd.read_csv(f"{path}/rejected_2007_to_2018Q4.csv")
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
    res = requests.post(f"http://{host}:5000/transaction", data=json.dumps(data))
    print(res)
    input()
    