import pandas as pd

# Step 1: Load the Data
data = pd.read_csv('inpatient.csv', sep='|')

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Step 2: Explore the Dataset
# Identify the columns related to medical codexes (e.g., ICD codes, DRG codes)
for col in data.columns:
    print(col)

icd_dgns_cd5 = data['ICD_DGNS_CD5']
icd_dgns_e_cd10 = data['ICD_DGNS_E_CD10']
icd_prcdr_cd4 = data['ICD_PRCDR_CD4']
prncpal_dgns_cd = data['PRNCPAL_DGNS_CD']
admtg_dgns_cd = data['ADMTG_DGNS_CD']
clm_drg_cd = data['CLM_DRG_CD']
clm_drg_outlier_stay_cd = data['CLM_DRG_OUTLIER_STAY_CD']
hcpcs_cd = data['HCPCS_CD']

# Step 3: Analyze the Frequency of Each Unique Value
# Calculate the frequency of unique values in each codex column

# Frequency count for ICD codes
icd_dgns_cd5_frequency = icd_dgns_cd5.value_counts()
print("ICD_DGNS_CD5 Frequency:\n", icd_dgns_cd5_frequency)

icd_dgns_e_cd10_frequency = icd_dgns_e_cd10.value_counts()
print("ICD_DGNS_E_CD10 Frequency:\n", icd_dgns_e_cd10)

icd_prcdr_cd4_frequency = icd_prcdr_cd4.value_counts()
print("ICD_PRCDR_CD4 Frequency:\n", icd_prcdr_cd4)

# Frequency count for DRG codes
drg_frequency = drg_codes.value_counts()
print("DRG Codes Frequency:\n", drg_frequency)

# Frequency count for HCPCS codes
# hcpcs_frequency = hcpcs_codes.value_counts()
# print("HCPCS Codes Frequency:\n", hcpcs_frequency)

# Step 4: Handle Missing Data (if any)
# Check for missing values in codex-related columns
missing_icd_dgns_cd5 = icd_dgns_cd5.isnull().sum()


print(f"Missing ICD Codes: {missing_icd_dgns_cd5}")
print(f"Missing DRG Codes: {missing_drg}")
print(f"Missing HCPCS Codes: {missing_hcpcs}")

# Example of handling missing data by filling with a placeholder
icd_dgns_cd5.fillna('MISSING', inplace=True)
data['DRG_CODE'].fillna('MISSING', inplace=True)
data['HCPCS_CODE'].fillna('MISSING', inplace=True)

# Step 5: Summary of Findings
# Provide a summary of the most common codes
# Here we'll just print the top 5 most common codes for each category
print("Top 5 Most Common ICD Codes:\n", icd_dgns_cd5_frequency.head())

# Additional Analysis Example
# Are there any patterns? For instance, let's see if certain DRG codes are more common
# when ICD codes are specific values (e.g., 'E11' for Type 2 Diabetes)
diabetes_related = data[icd_dgns_cd5.str.contains('E11', na=False)]
common_drg_for_diabetes = diabetes_related['DRG_CODE'].value_counts()
print("Most Common DRG Codes for Patients with ICD Code E11 (Type 2 Diabetes):\n", common_drg_for_diabetes)