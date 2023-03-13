from time import sleep
from datetime import datetime

START_DATE = datetime(2021, 7, 13)
END_DATE = datetime(2036, 7, 12, hour=23, minute=59, second=59)
KMS = 11269

try:
    while True:
        SECONDS = (datetime.now() - START_DATE).total_seconds()
        MINUTES = (datetime.now() - START_DATE).total_seconds() / 60
        HOURS = (datetime.now() - START_DATE).total_seconds() / 60 / 60
        DAYS = (datetime.now() - START_DATE).total_seconds() / 60 / 60 / 24
        MONTHS = (datetime.now() - START_DATE).total_seconds() / 60 / 60 / 24 / 30.4375
        YEARS = (datetime.now() - START_DATE).total_seconds() / 60 / 60 / 24 / 365
        YEARS_LEFT = (END_DATE - datetime.now()).total_seconds() / 60 / 60 / 24 / 365
        TOTAL_KMS = KMS / YEARS * YEARS_LEFT + KMS
        try:
            print(f""" Seconds: {round(SECONDS)}, {round(KMS/SECONDS, 12):12.12f} \
Minutes: {round(MINUTES)}, {round(KMS/MINUTES, 10):10.10f} \
Hours: {round(HOURS)}, {round(KMS/HOURS, 8):8.8f} \
Days:{round(DAYS)}, {round(KMS/DAYS, 7):7.7f} \
Month: {round(MONTHS)}, {round(KMS/MONTHS, 5):5.5f} \
Year: {round(YEARS)}, {round(KMS/YEARS,4):4.4f} \
Total KMs: {round(TOTAL_KMS, 1):6.1f}""", end="\r")
        except ZeroDivisionError:
            ...
        sleep(0.95)
except KeyboardInterrupt:
	YEARS = (datetime.now() - START_DATE).total_seconds() / 60 / 60 / 24 / 365
	YEARS_LEFT = (END_DATE - datetime.now()).total_seconds() / 60 / 60 / 24 / 365
	TOTAL_KMS = KMS / YEARS * YEARS_LEFT + KMS
	print(f""" Total KMs: {round(TOTAL_KMS, 1):6.1f}                                                                                                                                                    """, end="\n")
