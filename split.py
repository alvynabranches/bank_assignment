import os
import json
import math
import pandas as pd
from tqdm import tqdm

host = "34.123.210.194"
path = "."
folder = os.path.join(os.path.dirname(__file__), "data")
df = pd.read_csv(f"{path}/rejected_2007_to_2018Q4.csv")
print(f"Done Loading Document with {len(df)} records.")
data = df.to_dict("records")
print(f"Done converting to JSON format.")
del df
print(f"Done deleting df")

if not os.path.isdir(folder): os.mkdir(folder)
for n, d in tqdm(enumerate(data), total=len(data)):
	file = f"{folder}/{n:010}.json"
	if not os.path.isfile(file):
		data = {}
		data["amount_requested"] = d["Amount Requested"]
		data["application_date"] = str(d["Application Date"])
		data["loan_title"] = d["Loan Title"]
		data["risk_score"] = 0 if math.isnan(d["Risk_Score"]) else d["Risk_Score"]
		data["debt_to_income_ratio"] = d["Debt-To-Income Ratio"]
		data["zip_code"] = d["Zip Code"]
		data["state"] = d["State"]
		data["employment_length"] = d["Employment Length"]
		data["policy_code"] = d["Policy Code"]
		json.dump(data, open(file, 'w'), indent=4)

