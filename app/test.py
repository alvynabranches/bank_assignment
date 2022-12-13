import pandas as pd

data = {'id': None, 'amount_requested': 25000.0, 'application_date': '2018-08-31', 'loan_title': 'Debt consolidation', 'risk_score': 665.0, 'debt_to_income_ratio': '22.69%', 'zip_code': '464xx', 'state': 'IN', 'employment_length': '< 1 year', 'policy_code': 0.0}

df = pd.DataFrame(data, index=[0])