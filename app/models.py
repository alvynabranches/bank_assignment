from sqlalchemy import Table, Column, Integer, String, Float
from db import meta

transactions = Table(
    "transactions", meta, 
    Column("id", Integer, primary_key=True),
    Column("member_id", Integer), 
    Column("loan_amnt", Integer),
    Column("funded_amnt", Integer),
    Column("funded_amnt_inv", Integer),
    Column("term", String(64)),
    Column("int_rate", Float),
    Column("installment", Float),
    Column("grade", String(8)),
    Column("sub_grade", String(8)),
    Column("emp_title", String(64)),
    Column("emp_length", String(32)),
    Column("home_ownership", String(32)),
    Column("annual_inc", Float),
    Column("verification_status", String(32)),
    Column("issue_d", String(32)),
    Column("loan_status", String(32)),
    Column("pymnt_plan", String(32)),
    Column("url", String(128)),
    Column("desc", String(1024)),
    Column("purpose", String()),
    Column("title", String()),
    Column("zip_code", String()),
    Column("addr_state", String()),
    Column("dti", Float),
    Column("delinqa_2yrs", Float),
    Column("earliest_cr_line", String),
    Column("fico_range_low", Float),
    Column("fico_range_high", Float),
    Column("inq_last_6mths", Integer),
    Column("mths_since_last_delinq", Float),
    Column("mths_since_last_record", Float),
    Column("open_acc", Float),
    Column("pub_rec", Float),
    Column("revol_bal", Float),
    Column("revol_util", Float),
    Column("total_acc", Float),
    Column("initial_list_status", String),
    Column("out_prncp", Float),
    Column("out_prncp_inv", Float),
    Column("total_pymnt", Float),
    Column("total_pymnt_inv", Float),
    Column("total_rec_prncp", Float),
    Column("total_rec_int", Float),
    Column("total_rec_late_fee", Float),
    Column("recoveries", Float),
    Column("collection_recovery_fee", Float),
    Column("last_pymnt_d", String),
    Column("last_paymnt_amnt", Float),
    Column("next_pymnt_d", String),
    Column("last_credit_pull_d", String),
    Column("last_fico_range_high", Float),
    Column("last_fico_range_low", Float),
    Column("collections_12_mths_ex_med", Float),
    Column("mths_since_last_major_derog", Float),
    Column("policy_code", Float),
    Column("application_type", String),
    Column("annual_income_joint", Float),
    Column("dti_joint", Float),
    Column("verification_status_joint", String),
    Column("acc_now_delinq", Float),
    Column("tot_coll_amt", Float),
    Column("tot_cur_bal", Float),
    Column("open_acc_6m", Float),
    Column("open_act_il", Float),
    Column("open_il_12m", Float),
    Column("open_il_24m", Float),
    Column("mths_sinc_rcnt_il", Float),
    Column("total_bal_il", Float),
    Column("il_util", Float),
    Column("open_rv_12m", Float),
    Column("open_rv_24m", Float),
    Column("max_bal_bc", Float),
    Column("all_util", Float),
    Column("total_rev_hi_lim", Float),
    Column("inq_fi", Float),
    Column("total_cu_tl", Float),
    Column("inq_last_12m", Float),
    Column("acc_open_past_24mths", Float),
    Column("avg_cur_bal", Float),
    Column("bc_open_to_buy", Float),
    Column("bc_util", Float),
    Column("chargeoff_within_12_mths", Float),
    Column("delinq_amnt", Float),
    Column("mo_sin_old_il_acct", Float),
    Column("mo_sin_old_rev_tl_op", Float),
    Column("mo_sin_rcnt_rev_tl_op", Float),
    Column("mo_sin_rcnt_tl", Float),
    Column("mort_acc", Float),
    Column("mths_sinc_recent_bc", Float),
    Column("mths_since_recent_bc_dlq", Float),
    Column("mths_since_recent_inq", Float),
    Column("mths_since_recent_revol_delinq", Float),
    Column("num_accts_ever_120_pd", Float),
    Column("num_actv_bc_tl", Float),
    Column("num_actv_rev_tl", Float),
    Column("num_bc_sats", Float),
    Column("num_bc_tl", Float),
    Column("num_il_tl", Float),
    Column("num_op_rev_tl", Float),
    Column("num_rev_accts", Float),
    Column("num_rev_tl_bal_gt_0", Float),
    Column("num_sats", Float),
    Column("num_tl_120dpd_2m", Float),
    Column("num_tl_30dpd", Float),
    Column("num_tl_90g_dpd_24m", Float),
    Column("nu_tl_op_past_12m", Float),
    Column("pct_tl_nvr_dlq", Float),
    Column("percent_bc_gt_75", Float),
    Column("pub_rec_bankruptcies", Float),
    Column("tax_liens", Float),
    Column("tot_hi_cred_lim", Float),
    Column("total_bal_ex_mort", Float),
    Column("total_bc_limit", Float),
    Column("total_il_high_credit_limit", Float),
    Column("revol_bal_joint", Float),
    Column("sec_app_fico_range_low", Float),
    Column("sec_app_fico_range_high", Float),
    Column("sec_app_earliest_cr_line", Float),
    Column("sec_app_int_last_mths", Float),
    Column("sec_app_mort_acc", Float),
    Column("sec_app_open_acc", Float),
    Column("sec_app_revol_util", Float),
    Column("sec_app_open_acc_il", Float),
    Column("sec_app_num_rev_accts", Float),
    Column("sec_app_chargeoff_within_12_mths", Float),
    Column("sec_app_collections_12_mths_ex_med", Float),
    Column("hardship_flag", String),
    Column("hardship_type", String),
    Column("hardship_reason", String),
    Column("hardship_status", String),
    Column("deferral_term", Float),
    Column("hardship_amount", Float),
    Column("hardship_start_date", String),
    Column("hardship_end_date", String),
    Column("payment_plan_start_date", String),
    Column("hardship_length", Float),
    Column("hardship_dpd", Float),
    Column("hardship_loan_status", String),
    Column("orig_projected_additional_accrued_interest", Float),
    Column("hardship_payoff_balance_amount", Float),
    Column("hardship_last_payment_amount", Float),
    Column("disbursement_method", String),
    Column("debt_settlement_flag", String),
    Column("debt_settlement_flag_date", String),
    Column("settlement_status", String),
    Column("settlement_date", String),
    Column("settlement_amount", Float),
    Column("settlement_percentage", Float),
    Column("settlement_term", Float),
    Column("annual_inc_MA50", Float)
)
