# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data_file=path # path for the file
data=np.genfromtxt(data_file, delimiter=",", skip_header=1)

print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
print(new_record)
#Code starts here
census = np.concatenate((data,new_record))


# --------------
#Code starts here
age = np.array([census[:,0]])
max_age = age.max()
min_age = age.min()
age_mean = np.mean(age)
age_std = np.std(age)


# --------------
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0 = np.size(race_0[:,2])
len_1 = np.size(race_1[:,2])
len_2 = np.size(race_2[:,2])
len_3 = np.size(race_3[:,2])
len_4 = np.size(race_4[:,2])

if len_0 < min(len_1, len_2, len_3, len_4):
    minority_race = 0
elif len_1 < min(len_2, len_3, len_4):
    minority_race = 1
elif len_2 < min(len_3, len_4):
    minority_race = 2
elif len_3 < len_4:
    minority_race = 3
else:
    minority_race = 4



# --------------
#Code starts here

senior_citizens = np.array(census[census[:,0]>60],dtype = int)
print(senior_citizens)
working_hours_sum = senior_citizens.sum(axis = 0)[6]
print(working_hours_sum)
senior_citizens_len = np.size(senior_citizens[:,0])
print(senior_citizens_len)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

high = np.array(census[census[:,1]>10], dtype = int)
print(high)
low = np.array(census[census[:,1]<=10], dtype = int)
print(low)
avg_pay_high = high.mean(axis=0)[7]
print(avg_pay_high)
avg_pay_low = low.mean(axis = 0)[7]
print(avg_pay_low)




