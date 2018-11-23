'''
Find best k by calculate cost function.
k was chosed when adding k has the least effect
on lowering the cost.
'''
import pandas as pd
from sklearn.cluster import KMeans

FILENAME_cost = "/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/dataset/medicalcost/processed_medicalcost.csv"
FILENAME_mice = "/Users/Jphild/Documents/Courses/Georgia Tech/Machine Learning/Assignment 3/dataset/mice protein/Data_Cortex_Nuclear.csv"

df_mice = pd.read_csv(FILENAME_mice)
df_cost = pd.read_csv(FILENAME_cost)

df_mice.drop("MouseID", axis=1, inplace=True)
df_mice.drop("Treatment", axis=1, inplace=True)
df_mice.drop("Behavior", axis=1, inplace=True)
df_mice.drop("class", axis=1, inplace=True)

df_cost.drop("Unnamed: 0", axis=1, inplace=True)
df_cost.drop("charges", axis=1, inplace=True)

print(df_mice)
print(df_cost)


