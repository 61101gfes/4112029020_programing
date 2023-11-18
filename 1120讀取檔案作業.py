import pandas
import matplotlib.pyplot as plt
import numpy
housing=pandas.read_csv(r"C:\Users\User\Downloads\HousingData.csv")
avg=housing['B'].mean()
sum=0
count=0
for i in housing['B']:
    count+=1
    a=(i-avg)**2
    
    sum+=a
u=(sum/count)

print(f"資料B的平均:{avg}")
print(f"資料B的標準差:{u**0.5}")
indus_data = housing['INDUS']

plt.hist(indus_data, bins=30, color='blue',edgecolor='black')  
plt.title('Histogram of INDUS ')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
