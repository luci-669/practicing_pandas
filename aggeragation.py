import pandas as pd 

df = pd.read_csv("pokemon.csv")

# studying about aggergate function 


#Aggergate func that apply to whole df 

# print(df.sum(numeric_only= True))
# print(df.mean(numeric_only= True))
# print(df.min(numeric_only= True))
# print(df.max(numeric_only= True))
# print(df.count())

# for single coulum 
# print(df["Height"].sum())
# print(df["Height"].mean())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

# use of groupby func 

group = df.groupby("Type1")

print(group["Height"].sum())# you can apply aggergate func by making group of data 