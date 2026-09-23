import pandas as pd 

df = pd.read_csv("pokemon.csv", index_col=["Name"])

# print(df.to_string())  

# selection by colum

# print(df["Name"].to_string()) 

# selecting multiple colums 

# print(df[["Name", "Weight" , "Height"]].to_string())

# selecting row 

# print(df.loc["Pikachu"])

# print(df.loc["Charizard" : "Blastoise", ["Weight", "Height"]])

# selecting using index value 

# print(df.iloc[1:20:2 , 0:4]) # start : end : skip  , colum start to end 

# exersise search a pokemon by name by user input


while(True):
    pokemon = input("Enter a Pokemon name to Know abt or enter 0 to end : ")
    if pokemon == "0" :
            break
    try :
        print(df.loc[pokemon])
    except :
        print(f"{pokemon} Not Found might check spelling")
    