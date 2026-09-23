import pandas as pd

# a series in panda is one dementional laybled array

data = [100,110,222,250,155]

series = pd.Series(data, index = ['a','b','c','d','e'])


series.loc['b'] +=50

print(series.loc['c'])
print(series[series >= 150]) # we can filtter acc to condition 
print(series)
# can apply same concept in a dic 
