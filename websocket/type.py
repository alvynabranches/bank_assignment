import strawberry

from db import conn
from enum import Enum
from typing import Optional
from datetime import datetime
from models import transactions

class ApplicationType(Enum):
    individual = "Individual"
    joint = "Joint App"

@strawberry.type
class Transaction:
    id: int
    member_id: Optional[int]
    loan_amnt: int
    funded_amnt: int
    funded_amnt_inv: int
    term: str
    int_rate: float
    installment: float
    grade: str
    sub_grade: str
    emp_title: str
    emp_length: str
    home_ownership: str
    annual_inc: float
    verification_status: str
    issue_d: str
    loan_status: str
    pymnt_plan: str
    url: str
    desc: str
    purpose: str
    title: str
    zip_code: str
    addr_state: str
    dti: float
    delinqa_2yrs: float
    earliest_cr_line: str
    fico_range_low: float
    fico_range_high: float
    inq_last_6mths: int
    mths_since_last_delinq: Optional[float]
    mths_since_last_record: Optional[float]
    open_acc: float
    pub_rec: Optional[float] = 0.0
    revol_bal: float
    revol_util: float
    total_acc: float
    initial_list_status: str
    out_prncp: Optional[float] = 0.0
    out_prncp_inv: Optional[float] = 0.0
    total_pymnt: float
    total_pymnt_inv: float
    total_rec_prncp: float
    total_rec_int: float
    total_rec_late_fee: Optional[float] = 0.0
    recoveries: Optional[float] = 0.0
    collection_recovery_fee: Optional[float] = 0.0
    last_pymnt_d: str | datetime
    last_paymnt_amnt: float
    next_pymnt_d: Optional[str | datetime] = None
    last_credit_pull_d: str | datetime
    last_fico_range_high: float
    last_fico_range_low: float
    collections_12_mths_ex_med: Optional[float] = 0.0
    mths_since_last_major_derog: float = None
    policy_code: Optional[float] = 1.0
    application_type: Optional[ApplicationType | str] = "Individual"
    annual_income_joint: Optional[float] = None
    dti_joint: Optional[float] = None
    verification_status_joint: Optional[str] = None
    acc_now_delinq: Optional[float] = 0.0
    tot_coll_amt: Optional[float] = 0.0
    tot_cur_bal: float
    open_acc_6m: Optional[float] = 0.0
    open_act_il: float
    open_il_12m: Optional[float] = 0.0
    open_il_24m: float
    mths_sinc_rcnt_il: float
    total_bal_il: float
    il_util: Optional[float] = None
    open_rv_12m: float
    open_rv_24m: float
    max_bal_bc: float
    all_util: float
    total_rev_hi_lim: float
    inq_fi: float
    total_cu_tl: float
    inq_last_12m: float
    acc_open_past_24mths: float
    avg_cur_bal: float
    bc_open_to_buy: float
    bc_util: float
    chargeoff_within_12_mths: Optional[float] = 0.0
    delinq_amnt: Optional[float] = 0.0
    mo_sin_old_il_acct: float
    mo_sin_old_rev_tl_op: float
    mo_sin_rcnt_rev_tl_op: float
    mo_sin_rcnt_tl: float
    mort_acc: float
    mths_sinc_recent_bc: float
    mths_since_recent_bc_dlq: Optional[float] = None
    mths_since_recent_inq: Optional[float] = None
    mths_since_recent_revol_delinq: Optional[float] = None
    num_accts_ever_120_pd: Optional[float] = 0.0
    num_actv_bc_tl: float
    num_actv_rev_tl: float
    num_bc_sats: float
    num_bc_tl: float
    num_il_tl: float
    num_op_rev_tl: float
    num_rev_accts: float
    num_rev_tl_bal_gt_0: float
    num_sats: float
    num_tl_120dpd_2m: Optional[float | None] = 0.0
    num_tl_30dpd: Optional[float] = 0.0
    num_tl_90g_dpd_24m: Optional[float] = 0.0
    nu_tl_op_past_12m: float
    pct_tl_nvr_dlq: float
    percent_bc_gt_75: float
    pub_rec_bankruptcies: Optional[float] = 0.0
    tax_liens: Optional[float] = 0.0
    tot_hi_cred_lim: float
    total_bal_ex_mort: float
    total_bc_limit: float
    total_il_high_credit_limit: float
    revol_bal_joint: Optional[float | None] = None
    sec_app_fico_range_low: Optional[float] = None
    sec_app_fico_range_high: Optional[float] = None
    sec_app_earliest_cr_line: Optional[float] = None
    sec_app_int_last_mths: Optional[float] = None
    sec_app_mort_acc: Optional[float] = None
    sec_app_open_acc: Optional[float] = None
    sec_app_revol_util: Optional[float] = None
    sec_app_open_acc_il: Optional[float] = None
    sec_app_num_rev_accts: Optional[float] = None
    sec_app_chargeoff_within_12_mths: Optional[float] = None
    sec_app_collections_12_mths_ex_med: Optional[float] = None
    hardship_flag: Optional[str] = "N"
    hardship_type: Optional[str] = None
    hardship_reason: Optional[str] = None
    hardship_status: Optional[str] = None
    deferral_term: Optional[float] = None
    hardship_amount: Optional[float] = None
    hardship_start_date: Optional[str | datetime] = None
    hardship_end_date: Optional[str | datetime] = None
    payment_plan_start_date: Optional[str | datetime] = None
    hardship_length: Optional[float] = None
    hardship_dpd: Optional[float] = None
    hardship_loan_status: Optional[str] = None
    orig_projected_additional_accrued_interest: Optional[float] = None
    hardship_payoff_balance_amount: Optional[float] = None
    hardship_last_payment_amount: Optional[float] = None
    disbursement_method: Optional[str] = "Cash"
    debt_settlement_flag: Optional[str] = "N"
    debt_settlement_flag_date: Optional[str | datetime] = None
    settlement_status: Optional[str] = None
    settlement_date: Optional[str | datetime] = None
    settlement_amount: Optional[float] = None
    settlement_percentage: Optional[float] = None
    settlement_term: Optional[float] = None
    annual_inc_MA50: Optional[float] = None
    annual_inc_MA100: Optional[float] = None

@strawberry.type
class Query:
    @strawberry.field
    def transaction(self, info, id: int) -> Transaction:
        return conn.execute(transactions.select().where(transactions.c.id == id)).fetchall()

    def transactions(self, info) -> Transaction:
        return conn.execute(transactions.select()).fetchall()

class Mutation:
    @strawberry.type
    def create_transaction(self, info, id: int) -> Transaction:
        ...