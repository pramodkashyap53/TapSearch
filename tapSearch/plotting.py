# In this data assignment you will transform raw data from IPL into graphs that will convey some meaning / analysis. For each part of this assignment you will have 2 parts -

# Download both csv files from https://www.kaggle.com/manasgarg/ipl

# Code python functions that will transform the raw csv data into a data structure in a format suitable for plotting with matplotlib.

# Generate the following plots ...

# 1. Plot the number of matches played per year of all the years in IPL.
# 2. Plot a stacked bar chart of matches won of all teams over all the years of IPL.
# 3. For the year 2016 plot the extra runs conceded per team.
# 4. For the year 2015 plot the top economical bowlers.
# 5. Discuss a "Story" you want to tell with the given data. As with part 1, prepare the data structure and plot with matplotlib.

import csv, json
import matplotlib.pyplot as plt
import numpy as np
# %cd d:\sri\python1
csvFilePath = "matches.csv"
jsonFilePath = "matches.json"


arr = []
#read the csv and add the arr to a arrayn

with open (csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)

print(arr)

# write the data to a json file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))

with open('matches.json') as f:
    
      matches = json.load(f)
  
yearObj={}
for match in matches:
    print(match['id'])
    if(match['season'] not in yearObj):
        yearObj[match['season']]=1
    else:
        yearObj[match['season']]+=1

print(yearObj)

l=[]
for year in yearObj:
    l.append(year)
    
def plot_bar_x():
    # this is for plotting purpose
    
    plt.bar(range(len(yearObj)), list(yearObj.values()), align='center')
    plt.xticks(range(len(yearObj)), list(yearObj.keys()))
    plt.title('ipl match per season')
    plt.show()
plot_bar_x()