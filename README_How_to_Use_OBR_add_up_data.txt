# Manual for the OBR-Add-Up-Data program
# 
# Copyright 2016 Soren Heinze
# soerenheinze@gmx.de
# 5B1C 1897 560A EF50 F1EB 2579 2297 FAE4 D9B5 2A35
# 
# This work is licensed under a Creative Commons 
# Attribution-ShareAlike 4.0 International License.
# 
# You are free to:
# Share — copy and redistribute the material in any medium or format
# Adapt — remix, transform, and build upon the material for any purpose, 
# even commercially.
# The licensor cannot revoke these freedoms as long as you follow the license 
# terms.
# 
# Under the following terms:
# Attribution — You must give appropriate credit, provide a link to the 
# license, and indicate if changes were made. You may do so in any reasonable 
# manner, but not in any way that suggests the licensor endorses you or your 
# use.
# 
# ShareAlike — If you remix, transform, or build upon the material, you must 
# distribute your contributions under the same license as the original.
# 
# No additional restrictions — You may not apply legal terms or technological 
# measures that legally restrict others from doing anything the license permits.
# 
# Notices:
# You do not have to comply with the license for elements of the material in 
# the public domain or where your use is permitted by an applicable exception 
# or limitation.
# No warranties are given. The license may not give you all of the permissions 
# necessary for your intended use. For example, other rights such as publicity, 
# privacy, or moral rights may limit how you use the material.
# 
# This is a human-readable summary of (and not a substitute for) the license. 
# See https://creativecommons.org/licenses/by-sa/4.0/legalcode for the 
# whole license text.



How to use the OBR-Add-Up-Data program


i. It is assumed that GNU/Linux users know their ways around basic procedures. 
So these instructions concentrate in some parts on windows users.

ii. This procedure was tested on a 64-bit, windows 7 Professional, Service pack 1.
operating system.

iii. It is assumed that python and all the necessary modules are installed. See 
the relevant document regarding this issue.

iv. For this document it is assumed that the python program 
(the OBR_add_up_data.py-file) is saved under "C:\OBR_add_up_data".
Of course it can be stored anywhere on the computer, the instructions given 
below must then just be adapted.

v. The python program requires NO installation!

vi. It is assumed that the OBR_noise_reducer.py program was used before this 
python program is executed. This means the following
- All files contain JUST the data in a table and NO additional data on top 
	or bottom of this table.
- All filenames are just a running number, followed by "_noise_reduced".
	E.g. "0023_noise_reduced"; this program relies on that!

viii. ATTENTION: It is assumed that the folder in which the files mentioned
in point vii contains JUST these files and NO subfolders or other files.

viii. The python program is licensed under the GNU GPL version 3. This means 
that you as the user are allowed to change it according to your needs, without
asking for permission.
See http://www.gnu.org/licenses/ for more information.


## ## ## ## ## ## ## ## ## ## ## ## ##
Algorithm how to use the OBR_add_up_data-program to create one file that
contains the added up data from many files for easier use in data visualization
programs.
## ## ## ## ## ## ## ## ## ## ## ## ##

1. Open a command line interface
	- press and hold the <windows> button and press "R" (<windows-button> + R)
	- write "cmd" into the line in the small window that appears (without the 
		quotation marks). It will not be mentioned further that the quoation marks
		are not to be written, except when explicitely stated
	- The default windows command line interface, which will be called 
		"the shell" from now on, opens. Any other shell can also be used.

2. Change to the location of the python program on the shell
	- write "cd C:\OBR_add_up_data" on the shell and press ENTER.
		Now the shell is operating in the folder in which the python program is
		located.
		If the python program is saved at a different location, of course this 
		different location has to be stated.

3. Start the Add-up-data program
	- write "python OBR_add_up_data.py" on the shell and press ENTER.
	- The Add-up-data program has started. 

4. Input the correct parameters for Filesorter program
	- Basically follow the instructions on screen. 
	- ATTENTION: The noise reducing algorithm does NOT check the very first
		file for noise. 
		THIS HAS TO BE DONE MANUALLY!
		However, sine the Add-up-data program needs a "0001_noise_reduced"-file
		the noise reducing program more or less just copies this first file
		to these folders.
		But this means, that this file probably contains noise.
		However, having the automated measurement program in mind for which all
		these small programs were created, the very first file is most often 
		a file directly taken when the measurement starts and usually does NOT 
		contain outliers.
	- Input the location of the analyzed files.
		E.g. C:\Users\Username\Desktop\Sample_23017\Noise_reduced_after_manual_correction
		ATTENTION: It is very important that just "_noise_reduced"-files are in
		this folder.
		If this is not the case the program will not work. 
		Hence, delete all other files!
	- press ENTER


Congratulations you have now two files which should be easier to import
into data visualization programs (like e.g. SciDAVIs). 
One file that contains all the NOT added up data from the many files: "0000_ALL_IN_ONE_NOT_ADDED_UP.txt", and another file that contains these 
values added up from measurement to measurement: "0000_ALL_ADDED_UP.txt"
The delimiter between the files is a tab.









