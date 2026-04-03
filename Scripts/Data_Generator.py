import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_fct_raw_data(rows=50000):
provinces = ['QC', 'ON', 'BC', 'AB', 'NB', 'NS']
banks = ['RBC', 'NBC', 'BMO', 'ScotiaBank', 'Fairstone', 'TD']
notaries_qc = ['Maitre Belanger', 'Maitre Cote', 'Maitre Lavoie', 'Maitre Tremblay']
lawyers_roc = ['Smith & Co', 'Maritime Legal', 'Ontario Title Law', 'West Coast Legal']

data = []
start_date = datetime(2025, 1, 1)

for i in range(rows):
file_id = f"FCT-{700000 + i}"
province = np.random.choice(provinces, p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05])
bank = np.random.choice(banks, p=[0.2, 0.2, 0.15, 0.15, 0.1, 0.2])
refi_type = np.random.choice(['Internal', 'External'], p=[0.7, 0.3])
disbursement = random.randint(150000, 750000)

# 1. Date Received
received_date = start_date + timedelta(days=np.random.randint(0, 400))

# 2. Funding Logic (Applying your 2-3 day Fairstone rule)
if bank == 'Fairstone':
funding_days = np.random.randint(2, 4)
delay_reason = "None (Pre-scheduled)"
else:
funding_days = np.random.randint(12, 18)
delay_reason = "None"

# Simulated internal bottleneck (FCT's fault) for 5% of files
if random.random() < 0.05:
funding_days += 10
delay_reason = "Internal: Processing Backlog"
if refi_type == 'External':
funding_days += 7
delay_reason = "External: Payout Delay"
if province == 'QC' and random.random() < 0.10:
funding_days += 5
delay_reason = "Lender: Missing Docs"

funding_date = received_date + timedelta(days=funding_days)

# 3. Maturity Date (often less than 21 days out from receipt)
maturity_date = received_date + timedelta(days=np.random.randint(5, 22))

# Legal Professionals based on region
legal_pro = random.choice(notaries_qc) if province == 'QC' else random.choice(lawyers_roc)
funding_confirmed = "Yes" if random.random() > 0.01 else "No - Bank Dispute"

# Notice that we do NOT generate Penalty or Processing days here!
data.append([file_id, province, bank, refi_type, legal_pro, disbursement,
received_date, maturity_date, funding_date, delay_reason, funding_confirmed])

cols = ['File_ID', 'Province', 'Lender', 'Refi_Type', 'Professional', 'Disbursement',
'Date_Received', 'Maturity_Date', 'Date_Funded', 'Delay_Reason', 'Funds_Confirmed']

return pd.DataFrame(data, columns=cols)

# Run and generate the CSV file
df_fct = generate_fct_raw_data(50000)
df_fct.to_csv('FCT_Raw_Operations_Data.csv', index=False)
print("Success: Final Raw Dataset with 50,000 rows generated as 'FCT_Raw_Operations_Data.csv'!")

