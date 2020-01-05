# Siesta Structure/Coordinate Block Generation 

This script will read a .xyz file and prepare a coordinate file for Siesta. The coordinate block can be copied directly to the clipboard or saved as a text file. 

## Software/module Prerequisites:

1) Python version 3
2) Python modules (Glob, Pandas, Matplotlib)

## How to use:

1) Place script and .EIG file in a directory
2) Run Script
3) Provide atomic symbols of each atom **in the order you have defined in the Siesta Input file (This part is crucial!)**  
4) Add atoms as needed 
5) Save the processed structural data as a text file or directly copy to clipboard 
   * Note: clip board appears to give a cleaner copy of the text 

**NOTE: The script destroys the input .xyz file, so please do not use the original if you would like to have it for later use**.

I will fix this issue in the next version of the script  
