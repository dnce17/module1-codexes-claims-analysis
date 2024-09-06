import pandas as pd

# Step 1: Load the Data
data = pd.read_csv('inpatient.csv', sep='|')

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Step 2: Explore the Dataset
# Identify the columns related to medical codexes (e.g., ICD codes, DRG codes)
for col in data.columns:
    print(col)

code_name_arr = [
    'ICD_DGNS_CD5',
    'ADMTG_DGNS_CD',
    'ICD_PRCDR_CD4',
    'PRNCPAL_DGNS_CD',
    'ADMTG_DGNS_CD',
    'CLM_DRG_CD',
    'CLM_DRG_OUTLIER_STAY_CD',
    'HCPCS_CD',
]

# Step 3: Analyze the Frequency of Each Unique Value
# Calculate the frequency of unique values in each codex column
def get_frequency(code_arr):
    for code_name in code_arr:
        # For formatting purposes
        print("-----------")
        print(f'{code_name} Frequency:\n {data[code_name].value_counts()}\n')

# Step 4: Handle Missing Data (if any)
# Check for missing values in codex-related columns
def check_missing_data(code_arr):
    for i, code_name in enumerate(code_arr):
        print(f'Missing {code_name}: {data[code_name].isnull().sum()}')

        if i == len(code_arr) - 1:
            print("\n")
    
# Handling missing data by filling with a placeholder
def handle_missing_data(code_arr):
    for code_name in code_arr:
        data[code_name].fillna('MISSING', inplace=True)

# Step 5: Summary of Findings
# Print the top 5 most common codes for each category
def get_common_codes(code_arr):
    for code_name in code_arr:
        print("-----------")
        print(f'Top 5 Most Common {code_name}:\n {data[code_name].value_counts().head()}\n')

get_frequency(code_name_arr)
check_missing_data(code_name_arr)
handle_missing_data(code_name_arr)
get_common_codes(code_name_arr)

# Additional Analysis Example
# Are there any patterns? E.g. if certain DRG codes are more common
# when ICD codes are specific values (e.g., 'E11' for Type 2 Diabetes)
icd_dgns_cd5 = data['ICD_DGNS_CD5']
cd5_code_1 = "N1830"
kidney_related = data[icd_dgns_cd5.str.contains(cd5_code_1, na=False)]
common_drg_for_kidney = kidney_related['CLM_DRG_OUTLIER_STAY_CD'].value_counts()
print("-----------")
print(f'Most Common Claim DRG Outlier Stay Codes for Patients with ICD Code {cd5_code_1} (Chronic Kidney Disease):\n {common_drg_for_kidney}\n')

cd5_code_2 = "I259"
heart_related = data[icd_dgns_cd5.str.contains(cd5_code_2, na=False)]
common_drg_for_heart = heart_related['CLM_DRG_OUTLIER_STAY_CD'].value_counts()
print("-----------")
print(f'Most Common Claim DRG Outlier Stay Codes for Patients with ICD Code {cd5_code_2} (Chronic Ischemic Heart Disease):\n {common_drg_for_heart}\n')