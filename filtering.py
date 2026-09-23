import pandas as pd 

df = pd.read_csv("pokemon.csv")

# filtering is putting condition and fillter the non needed data

short_pokemon = df[df["Height"] <= 1.0]
water_type = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")] # can use & operater to match condition


print(water_type.to_string())