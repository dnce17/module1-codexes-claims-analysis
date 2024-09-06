import pandas as pd

# Step 1: Load the Data
data = pd.read_csv('inpatient.csv', sep='|')

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Step 2: Explore the Dataset
# Identify the columns related to medical codexes (e.g., ICD codes, DRG codes)
for col in data.columns:
    print(col)

# Line break
print()

code_name_arr = [
    'ICD_DGNS_CD5',
    'ICD_DGNS_E_CD10',
    'ICD_PRCDR_CD4',
    'PRNCPAL_DGNS_CD',
    'ADMTG_DGNS_CD',
    'CLM_DRG_CD',
    'CLM_DRG_OUTLIER_STAY_CD',
    'HCPCS_CD',
]

# def get_code_data(data_arr):
#     for code_name in code_name_arr:
#         data_arr.append(data[code_name])

# code_data_arr = []
# get_code_data(code_data_arr)

# Step 3: Analyze the Frequency of Each Unique Value
# Calculate the frequency of unique values in each codex column

# Frequency count for all codes
def get_frequency(code_arr):
    for i, code_name in enumerate(code_arr):
        print(f'{code_name} Frequency: {data[code_name].value_counts()}\n')
    
get_frequency(code_name_arr)

# Step 4: Handle Missing Data (if any)
# Check for missing values in codex-related columns
def check_missing_data(code_arr):
    for i, code_name in enumerate(code_arr):
        print(f'Missing {code_name}: {data[code_name].isnull().sum()}')

        if i == len(code_arr) - 1:
            print("\n")
    
check_missing_data(code_name_arr)


# TEST USE: to see if function works
# missing_code = data['ADMTG_DGNS_CD'].isnull().sum()
# print(missing_code)
# data['ADMTG_DGNS_CD'].sample(100)

# Example of handling missing data by filling with a placeholder
def handle_missing_data(code_arr):
    # for i, code_data in enumerate(code_arr):
    #     code_data.fillna('MISSING', inplace=True)
    #     print(code_data_arr[i])
    #     print("\n")

    for i, code_name in enumerate(code_arr):
        data[code_name].fillna('MISSING', inplace=True)
        print(f'{data[code_name]}\n')


handle_missing_data(code_name_arr)

# # Step 5: Summary of Findings
# # Provide a summary of the most common codes
# # Here we'll just print the top 5 most common codes for each category
# print('Top 5 Most Common ICD Codes:\n', icd_dgns_cd5_frequency.head())

# # Additional Analysis Example
# # Are there any patterns? For instance, let's see if certain DRG codes are more common
# # when ICD codes are specific values (e.g., 'E11' for Type 2 Diabetes)
# diabetes_related = data[icd_dgns_cd5.str.contains('E11', na=False)]
# common_drg_for_diabetes = diabetes_related['DRG_CODE'].value_counts()
# print('Most Common DRG Codes for Patients with ICD Code E11 (Type 2 Diabetes):\n', common_drg_for_diabetes)