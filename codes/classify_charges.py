'''
Add a new column to "medicalcost" dataset.
The new column is derived from "charges"
Charges were classified into 1, 2 or 3 based on 
the value
'''
import pandas as pd

df = pd.read_csv("processed_medicalcost.csv")
new_list = []
one_third = (df["charges"].max() - df["charges"].min()) / 3.0
print(df["charges"].min())
print(df["charges"].min() + one_third)
print(df["charges"].min() + one_third * 2)
print(df["charges"].max())
for ele in df["charges"]:
	if ele <= df["charges"].min() + one_third:
		new_list.append(1)
	elif ele <= df["charges"].min() + one_third * 2:
		new_list.append(2)
	else:
		new_list.append(3)

df["classified_charges"] = new_list
df.to_csv("medical_cost_classified.csv")