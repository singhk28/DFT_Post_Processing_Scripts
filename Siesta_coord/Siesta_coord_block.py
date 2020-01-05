# This script will read a .xyz file and prepare a coordinate file for Siesta
# The script is written in Python 3.7 


print("==========" * 5)
print("This script will read a .xyz file and prepare a coordinate file for Siesta")
print("This script is written by Kamalpreet Singh in Python V3")
print("==========" * 5)

##### Importing Modules #####
import glob
import os
import pandas as pd

###### Importing the File & Prepping the structure #####

find_file_name_list = glob.glob('*.xyz')                                          
file_name = str(find_file_name_list[0])                                           
print(file_name)


base = os.path.splitext(file_name)[0]
os.rename(file_name, base + ".txt")

find_file_name_list_txt = glob.glob('*.txt')                                              
file_name_txt = str(find_file_name_list_txt[0])                                           
print(file_name_txt)

coordinate_file = open (file_name_txt, 'r+')                                         
Lines = coordinate_file.readlines()
mod_lines = open('coord.csv', 'w').writelines(Lines[2:])


df = pd.read_csv("coord.csv", delim_whitespace=True, header = None)
df.columns = ['Atoms' ,'X', 'Y', 'Z']
print(df)

asking_atoms = 'y'
counting = 1

while asking_atoms == 'y' :
    atoms = input("Give atomic symbol of atom - Please provide atoms in same sequence as the Siesta input \n")
    df['Atoms'] = df['Atoms'].replace(atoms, counting)
    #print(df)
    asking_atoms = input("Do you want to add another atom? (y/n) \n")
    counting = counting + 1

Siesta_coord = df[['X', 'Y','Z','Atoms']]

print(Siesta_coord)

clipboard = input("Do you want to copy results to clipboard or save a text file (clip/text) \nNote: copying to clipboard gives cleaner data \n")


if clipboard == 'clip':
    Siesta_coord.to_clipboard(header = False, index = False ) 
elif clipboard == 'text' : 
    Siesta_coord.to_csv("Siesta_Coord.txt", sep =" ", header = False, index = False) 

 
print("\n") 
print("Good bye")





