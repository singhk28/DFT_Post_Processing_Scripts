# DFT Post Processing Scripts
This repo contains various python scripts I developed for post processing data from DFT calculations with various DFT packages (Ex: SIESTA, CP2k, VASP)

Current list of scripts:

1) NEB_plot.py - Create an energy diagram from NEB calculation (CP2K) 

2) SIESTA_coord.py - Create SIESTA coordination block for the input file from a XYZ file 

3) SIESTA_EIG.py - Plot EIG file to see the eigenvalue spectrum to visualize the spread of eigenvalues.

## How to run scripts:

1) Install Python version 3 (Preferrably 3.7) [https://www.python.org/downloads/release/python-370/]

   * Ensure python has been added to path when installing. 

2) Install the neccessary modules 

   In windows, this can be achieved by opening powershell and pasting the following pip commands for each required module:

   * Glob: comes built in with the python distribution 

   * Pandas: pip install pandas [https://pypi.org/project/pandas/]

   * MatplotLib: pip install matplotlib [https://pypi.org/project/matplotlib/] 
   
3) Open Powershell and navigate to the directory with the script and the required file (depending on DFT calculation of interest):

   In windows, this can be achieved by writing: **cd "path of directory"** 

4) Once in the correct directory, launch the script by writing: **python "script_name.py"** 

