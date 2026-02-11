import numpy as np
import pandas as pd
arr=np.array([10,20,5,6,30])
print("array:",arr)
print("sum",np.sum(arr))
print("mean",np.mean(arr))
print("multiply by 2:",arr*2)
data={
     "Name":["Kiran","Anita","Ravi"],
     "Age":[25,27,26],
     "City":["Bangalore","Chennai","Hyderabad"]
}
df=pd.Dataframe(data)
print(df)

print(df["name"])
print(df[df["Age"]>26])
df["Salary"]=[50000,600000,700000]
print(df)