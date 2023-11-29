import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

data = pd.read_csv("/content/HousingData.csv")

data = data.fillna(data.mean())
print(data.mean())

dx = data.drop(['MEDV'],axis=1)
dy = data['MEDV']

dx_std = StandardScaler().fit_transform(dx)
dx_train ,dx_test ,dy_train ,dy_test=train_test_split(dx_std , dy,test_size=0.2, random_state=0)
# 使用 KNN 回歸模型進行訓練
knn = KNeighborsRegressor()
knn.fit(dx_train,dy_train)
predictions = knn.predict(dx_test)
print(dy_test)
print(predictions)
print(knn.score(dx_train, dy_train))
print(knn.score(dx_test,dy_test))
