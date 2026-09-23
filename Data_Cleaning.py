import pandas as pd 

df = pd.read_csv("pokemon.csv")

# drop coulum
# df = df.drop(columns=["Legendary" , "No"])


#drop missing data 
# df = df.dropna(subset = ["Type2"])
# df = df.fillna({"Type2" : "None"})

# fixing inconsistance data 
# df["Type1"] = df["Type1"].replace({"Grass" : "Niggaa" , 
#                                    "Fire" : "Angggg"})

# #Santdrize text
# df["Name"] = df["Name"].str.lower()
# df["Name"] = df["Name"].str.upper()


# #fix data type 
# df["Legendary"] = df["Legendary"].astype(bool)

# remove duplicate value 
df = df.drop_duplicates()


print(df.to_string())

