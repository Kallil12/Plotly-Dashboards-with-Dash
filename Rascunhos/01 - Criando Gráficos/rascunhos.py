import pandas as pd
import numpy as np

df = pd.read_csv('salaries.csv')
print(df[['Name','Salary']])

print("O valor mínimo de salário é:",df['Salary'].min())

print("O valor médio de salário é:",df['Salary'].mean())

print("=====================")
# conditional filter

#series_of_bool = df['Age']>30
#print(df[series_of_bool])

print(df['Age']>30)
print(df[df['Age']>30])

print("=====================")

print(df['Age'].unique())
print(df['Age'].nunique())
print(df.columns)
print("====================================")

print(df.info())
print("====================================")

print(df.describe())
print("====================================")

matriz_teste = np.arange(0,10).reshape(5,2)
matriz_teste_2 = pd.DataFrame(data=matriz_teste, columns=['A','B'],index=[])
print(matriz_teste_2)