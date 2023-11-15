import numpy as np 
a=[1,2,3,4,5,6]
new=[a[i:i+2] for i in range(0,len(a),2)]
print(new)
  
max=max(a)
print(max)

2.
import pandas as pd
import numpy as np
new={'grammer':['python','java','go','NaN','python','C','C++'],'score':[1.0,'NaN','NaN',4.0,5.0,7.0,8.0]}
ar=pd.DataFrame(new)
ar['score'] = pd.to_numeric(ar['score'], errors='coerce')
print(ar)
ar.columns=['grammer','popularity']
ar.index=[1,2,3,4,5,6,7]
print(ar)
avg=ar['popularity'].mean()
print('平均:\n',avg)

3.
test={'a':[50,64,87],'b':[96,59,68],'c':[59,86,67]}
import numpy as np
import pandas as pd
df=pd.DataFrame(test)

df.index=['test1','test2','test3']
print(df)
df.T
print(df)

4.
import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np
tempature=[20,25,30,35]
sale=[12,16,22,34]
mp.xlabel('sale')
mp.ylabel('tempature')

mp.scatter(sale,tempature,color='red')
mp.show
mp.bar(sale,tempature,color=['red','green'])
mp.show


5.
import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np
mp.xlabel('x value')
mp.title('sin(x)')
x=np.linspace(0,10,100)
y=np.sin(x)
mp.plot(x,y,color='red')
mp.show



6.
import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np
import random
mp.xlabel('x value')
mp.title('Histogram')
mp.legend()

y=np.random.randn(1000)
x=np.arange(len(y))
mp.bar(x,y,color='green')
mp.show
