import pandas as pd

data = {
    "Name" : ["leon","Ray","Oni"],
    "Age"  : [18,20,17]
}
df = pd.DataFrame(data, index = ["Emp1", "Emp2", "Emp3"])

#add new coulum
df["Job"] = ["DayTrader", "Freelancer", "Devloper"]

# add a new row can add multiple row in a single variable
new_row = pd.DataFrame([{"Name" : "Luffy", "Age" : 22 , "Job" : "UI/UX"}], index = ["Emp4"])
df = pd.concat([df, new_row])
print(df)