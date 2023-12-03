import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

#data_gender=pd.read_csv("/content/gender_submission[1].csv")
data_test=pd.read_csv('/content/test[1].csv')
data_train=pd.read_csv('/content/train[1].csv')

data_train['Sex']=data_train['Sex'].map({'male':0,'female':1})
data_train['Embarked']=data_train['Embarked'].map({'S':3,'C':2,'Q':1})
dx=data_train.drop(['Survived','Name','Ticket','Cabin'],axis=1)
dx=dx.fillna(dx.mean())
dy=data_train['Survived']
dx_std=StandardScaler().fit_transform(dx)
#dx_train,dx_test,dy_train,dy_test=train_test_split(dx_std,dy,test_size=0.2,random_state=1)
x_test=data_test.drop(['Name','Cabin','Ticket'],axis=1)
x_test['Sex']=x_test['Sex'].map({'male':0,'female':1})
x_test['Embarked']=x_test['Embarked'].map({'S':3,'C':2,'Q':1})
x_test=x_test.fillna(x_test.mean())
x_test=StandardScaler().fit_transform(x_test)

#print(dx_std)
print('----------------------------')
#print(x_test)

knn=KNeighborsRegressor()
knn.fit(dx_std,dy)
predictions=knn.predict(x_test)
notsurvive_num=sum(predictions<1)





print(f"KNN score :\n{knn.score(dx_std,dy)}")
print(f"\n--------------------------------------\n")
print(f"Predictions(預估存活人數:{418-notsurvive_num} / {len(predictions)}) :\n{predictions }")