import os
import json
import requests
import pandas as pd
from tqdm import tqdm

df = pd.read_csv("/home/alvynabranches/Downloads/accepted_2007_to_2018Q4.csv", low_memory=False)

for n, d in tqdm(enumerate(df.to_dict("records")), total=len(df.to_dict("records"))):
    json.dump(d, open(os.path.join(os.path.dirname(__file__), "data", f"{n:010}.json")))
