# Module 1 Homework Assignment: Discovering Medical Codexes within Synthetic Medicare Fee-for-Service Claims Data

## Analysis Steps and Purpose of Each Code
NOTE: horizontal lines and line breaks (\n) are sometimes printed to increase readability in terminal

1. Imported pandas package to aid in analysis
2. Loaded data with the pandas .read_csv() function by inserting a local CSV file that I downloaded from the CMS site and using the | delimiter
3. data.head() is printed to display the first few rows of the dataset in order to understand its structure
4. Looped through data columns to see what column names exist
5. Explored the dataset and chose 8 unique types of medical codexes that I put into an array titled "code_name_arr"
6. Multiple functions are made in the order shown below. Each loops through the code_name_arr to obtain certain information, which are as follows:
    * get_frequency(code_arr) obtains and prints the frequency of unique values in each medical code
    * check_missing_data(code_arr) calculates and prints the total amount of missing values in each medical code
    * handle_missing_data(code_arr) uses the pandas .fillna function to fill missing data with a "MISSING" placeholder
    * To get summary of findings, get_common_codes(code_arr) prints the top 5 most common codes from each of the 8 medical codes
7. After defining the functions, they were all called using code_name_arr as their parameter
8. Additional analysis is conducted
    * Analysis 1
        * the "icd_dgns_cd5" variable was made to hold the data for claim diagnosis code 5 (ICD_DGNS_CD5)
        * the "kidney_related" variable uses "icd_dgns_cd5" to store the data of ICD_DGNS_CD5 that only contains ICD code "N1830" (chronic kidney disease) 
        * the "common_drg_for_kidney" variable uses "kidney_related" to determine the most common claim DRG outlier stay codes (CLM_DRG_OUTLIER_STAY_CD) when the ICD code is N1830
    * Analysis 2
        * the "heart_related" variable uses the previously defined "icd_dgns_cd5" to store the data of ICD_DGNS_CD5 that contains ICD code "I259" (chronic ischemic heart disease) 
        * the "common_drg_for_heart" variable uses "heart_related" to determine the most common CLM_DRG_OUTLIER_STAY_CD when the ICD code is I259

## Key Findings + Implications from Analysis
CLM_DRG_OUTLIER_STAY_CD indicates patients who are classified into specific diagnosis groups that have an unusually long hospital stay (day outlier) or significantly higher cost (cost outlier). For chronic kidney disease (N1830), the outlier out of 4338 patients is very minimal with no day outliers and only 2 patients who have cost outliers. The total outliers for this disease would be less than 1%.

On the other hand, the chronic ischemic heart disease (I259)'s outlier out of its 2515 patients is 5%. While this percentage may seem small, 5% of the current total US population (about 337 million as of 2024 based on US Census Bureau) would be about 17 million, which is fairly substantial. 

The implication that this finding could have for healthcare providers and policy makers is the need to examine why these patients are experiencing longer stays and higher costs alongside developing a course of action. Healthcare is generally considered to be very expensive in the US, which can discourage people from getting crucial care that they need. Those who receive care and undergo certain procedures may also end up with a bill that they cannot afford, which leads to stress on their end trying to pay off medical debt. This causes a vicious cycle as chronic stress is often linked with many health issues that may have people needing to receive care again and paying once more. 

## Challenges, Errors, and Exceptions
* Losing track of variables - There was a lot of copy and pasting going on in printing the frequency, summary of findings, and checking and handling missing values when following the starter code. I sometimes mixed up variable names and lost track of which ones I already copied over. Thus, I created functions to loop through the 8 codes in order to obtain the desired information and reduce redundancy.

* KeyError - When choosing the 8 unique medical codes, I sometimes ran into a KeyError when I wanted to display my selected code's data. I resolved this issue by printing out the columns of the loaded CSV in the terminal and choosing the codes from there rather than from the CMS codebook's table of contents. Not all of the variables that existed in the codebook existed in the loaded CSV, so that led to the KeyError.

* ImportError - I already installed pandas, but pandas was still not found. I typed "pip list" to make sure it was there, but that resulted in another error "pip: command not found." I resolved these issues by deleting the virtual environment (.venv) file and creating a new one; ultimately, pip worked and I was able to install pandas again and run it.
    * Resolving this issue also fixed a "SyntaxError", which had resulted from trying to print an f-string