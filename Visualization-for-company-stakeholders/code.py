# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
#print(data.head())
loan_status = data['Loan_Status'].value_counts()
print(loan_status)
loan_status.plot(kind = 'bar')

#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area' , 'Loan_Status']).size().unstack()
print(property_and_loan.head())
property_and_loan.plot(kind='bar', stacked= False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')

# Display plot
plt.xticks(rotation=45)
plt.show()



# --------------
#Code starts here
education_and_loan = data.groupby(['Education' ,'Loan_Status']).size().unstack()
plt.plot(kind ='bar' , stacked =True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation =45)
plt.show()


# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']
print(graduate.head())
not_graduate = data[data['Education'] == 'Not Graduate']
print(not_graduate.head())
graduate.plot(kind = 'density' ,label='Graduate')
not_graduate.plot(kind = 'density' ,label='Non Graduate')









#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2 , ax_3) = plt.subplots(3,1, figsize=(20,10))

data.plot(kind='scatter', x='ApplicantIncome', y='LoanAmount', ax=ax_1)
ax_1.set_title('Applicant Income')

data.plot(kind='scatter', x='CoapplicantIncome', y='LoanAmount', ax=ax_2)
ax_1.set_title('CoapplicantIncome')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data.plot(kind='scatter', x='ApplicantIncome', y='LoanAmount', ax=ax_3)
ax_1.set_title('ApplicantIncome')



