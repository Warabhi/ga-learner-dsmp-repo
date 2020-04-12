# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)



# code ends here


# --------------
# code starts here

banks = bank.drop(['Loan_ID'],axis = 1)
isn  = banks.isnull().sum(axis = 0)
print(isn)
bank_mode = banks.mode()
print(bank_mode)
#banks =banks.fillna(0)
#print(banks)
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)

print(banks)    
#code ends here


# --------------
# Code starts here

avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount', )
print(avg_loan_amount)


# code ends here



# --------------
# code starts here
loan_approved_se =((banks['Self_Employed']=='Yes')&(banks['Loan_Status']=='Y')).value_counts()
print(loan_approved_se)
loan_approved_nse = ((banks['Self_Employed']=='No')&(banks['Loan_Status']=='Y')).value_counts()
print(loan_approved_nse)
percentage_se = (56/614)*100
print(percentage_se)
percentage_nse = (366/614)*100
print(percentage_nse)
# code ends here


# --------------
# code starts here
def convert(x):
    return x/12
   
loan_term = banks["Loan_Amount_Term"].apply(convert)

count = 0
for i in range(0,len(loan_term)):
    if loan_term[i] >= 25:
        count+=1

big_loan_term = count



# code ends here


# --------------
# code starts here


loan_groupby = banks.groupby("Loan_Status")['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()



# code ends here


