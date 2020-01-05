# This script automatically plots .EIG file from SIESTA
# Script is written in Python v3 by Kamalpreet Singh 

print ("----------------------------------------------")
print ("----------------------------------------------")
print ("This script automatically plots .EIG file from SIESTA")
print ("Script is written in Python v3 by Kamalpreet Singh")
print ("----------------------------------------------")
print ("----------------------------------------------")

## Module Imports ##

import pandas as pd
import matplotlib.pyplot as plt
import glob 

## Reading/Finding Files ## 

find_file_eig = glob.glob('*.EIG') 
file_name_eig = str(find_file_eig[0]) 

## Parsing EIG File ##

eig_file = open (file_name_eig, 'r+')                                          
eig_lines = eig_file.readlines()                                               
eig_file.close() 
fermi = eval(eig_lines[0])
eig_data = eig_lines[2:]

## Reformating Data ##

data_points = []

for line in eig_data:
    data_point = line.split()
    data_points.append(data_point) 
    
# Flattening list 

eig_data2  = []

for d in data_points:
    for d2 in d:
        eig_data2.append(d2)
        
del eig_data2[0]   # Deleting useless info


## Creating DataFrame from List ## 

eig_df = pd.DataFrame(eig_data2, columns = ["EIG Values"])
eig_df["Height"] = 1

## Exporting DataFrame into CSV ##

# Note, could also directly plot from DataFrame but it seemed to take 
# really long time to go through the data 

user_eig_data = input ("What do you want to call the CSV data file? \n")
user_eig_data_name = user_eig_data +".csv"
eig_df.to_csv(user_eig_data_name, index = False)


## Importing newly made CSV ## 

find_file_csv = glob.glob('*.csv') 
file_name_csv = str(find_file_csv[0])
data = pd.read_csv(file_name_csv)

## Plotting Bar Graph ## 

given_title = input("What is the title you want to give to the graph? \n")


xmin = fermi - 1.5
xmax = fermi + 1.5

plt.figure(figsize=(6, 4))
plt.bar(data["EIG Values"],data["Height"], width = 0.005 , color = "black")
plt.title(given_title, fontsize = 32)
plt.xlim(xmin,xmax)
plt.ylim(0,1)
plt.tight_layout()
plt.show()