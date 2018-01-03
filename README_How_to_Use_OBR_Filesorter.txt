# Manual for the OBR-Filesorter program
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



How to use the OBR-Filesorter program


i. It is assumed that GNU/Linux users know their ways around basic procedures. 
So these instructions concentrate in some parts on windows users.

ii. This procedure was tested on a 64-bit, windows 7 Professional, Service pack 1.
operating system.

iii. It is assumed that python and all the necessary modules are installed. See 
the relevant document regarding this issue.

iv. The OBR program was from Luna Technologies and simply called 
"Optical Backscatter Reflectometer", software version 3.12.2.
Throughout this document this program will be called "the OBR program"

v. The OBR_Filesorter.py program will be called "the python program" or
"the filesorter" or something similar.

vi. For this document it is assumed that the python program 
(the OBR_Filesorter.py-file) is saved under "C:\OBR_Filesorter".
Of course it can be stored anywhere on the computer, the instructions given 
below must then just be adapted.

vii. This program just creates folders with certain names that will make
the use of subsequent automated programs (e.g. Noise_reducer.py) easier.
Also all files are sorted into the correct folders.

viii. The python program requires NO installation!

ix. It is assumed that the OBR measurement files were analyzed using the 
OBR_analyzer_simple.py-program. 
This means that files exist that have the keyword "_older_reference" in the
filename. 
Also it is assumed that the OBR backscatter amplitudes are saved in files
with the keyword "_Upper", while the property of interest (e.g. strain) files
are saved in files with the keyword "_Lower" (with and without 
"_older_reference").
This will be the case if the OBR_analyzer_simple.py program
was used for automated analysis in connection with the above mentioned
OBR measurement/analysis program.

xiii. The python program is licensed under the GNU GPL version 3. This means 
that you as the user are allowed to change it according to your needs, without
asking for permission.
See http://www.gnu.org/licenses/ for more information.


## ## ## ## ## ## ## ## ## ## ## ## ##
Algorithm how to use the OBR_Filesorter-program to automatically sort 
analyzed OBR files.
## ## ## ## ## ## ## ## ## ## ## ## ##

1. Open a command line interface
	- press and hold the <windows> button and press "R" (<windows-button> + R)
	- write "cmd" into the line in the small window that appears (without the 
		quotation marks). It will not be mentioned further that the quoation marks
		are not to be written, except when explicitely stated
	- The default windows command line interface, which will be called 
		"the shell" from now on, opens. Any other shell can also be used.

2. Change to the location of the python program on the shell
	- write "cd C:\OBR_Filesorter" on the shell and press ENTER.
		Now the shell is operating in the folder in which the python program is
		located.
		If the python program is saved at a different location, of course this 
		different location has to be stated.

3. Start the Filesorter
	- write "python OBR_Filesorter.py" on the shell and press ENTER.
	- The Filesorter program has started. 

4. Input the correct parameters for Filesorter program
	- Basically follow the instructions on screen. 
	- Input the location of the analyzed files.
		E.g. C:\Users\Username\Desktop\Sample_23017

Congratulations all files are now sorted into the correct folders.









