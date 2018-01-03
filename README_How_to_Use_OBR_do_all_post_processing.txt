# Manual for the  program
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



How to use the OBR-Analyzer program


i. It is assumed that GNU/Linux users know their ways around basic procedures. 
So these instructions concentrate in some parts on windows users.

ii. This procedure was tested on a 64-bit, windows 7 Professional, Service pack 1.
operating system.

iii. It is assumed that python and all the necessary modules are installed. See 
the relevant document regarding this issue.

iv. This program executes more or less just OBR-Filesorter.py, 
OBR_Noise_reducer.py and OBR_add_up_data.py. 
ATTENTION: ALL THESE FILES MUST BE IN THE SAME FOLDER AS THE OBR_do_all_post_processing.py-file!

v. For this document it is assumed that ALL python source files (programs)
are saved under "C:\OBR_do_all_post_processing".
Of course it can be stored anywhere on the computer, the instructions given 
below must then just be adapted.

vi. The python program requires NO installation!

vi. It is assumed that the OBR measurement files were analyzed using the 
OBR_analyzer_simple.py-program. 
This means that files exist that have the keyword "_older_reference" in the
filename. 
Also it is assumed that the OBR backscatter amplitudes are saved in files
with the keyword "_Upper", while the property of interest (e.g. strain) files
are saved in files with the keyword "_Lower" (with and without 
"_older_reference").
This will be the case if the OBR_analyzer_simple.py program
was used for automated analysis in connection with the OBR program from 
Luna Technologies (which was simply called "Optical Backscatter Reflectometer", 
software version 3.12.2).

viii. All the programs can also be run by themself. Please see the accompanying
manuals and python source files.

ix. The python program is licensed under the GNU GPL version 3. This means 
that you as the user are allowed to change it according to your needs, without
asking for permission.
See http://www.gnu.org/licenses/ for more information.


## ## ## ## ## ## ## ## ## ## ## ## ##
Algorithm how to use the OBR_do_all_post_processing-program to create meaningful folders and
sort the files into these folders, noise reduced the analyzed files and put
the data from many files into one file that contains the added up data and 
another file that contains the NOT added up data for easier use in 
data visualization programs.
## ## ## ## ## ## ## ## ## ## ## ## ##

0. Make sure that all python-files are in the same folder!

1. Open a command line interface
	- press and hold the <windows> button and press "R" (<windows-button> + R)
	- write "cmd" into the line in the small window that appears (without the 
		quotation marks). It will not be mentioned further that the quoation marks
		are not to be written, except when explicitely stated
	- The default windows command line interface, which will be called 
		"the shell" from now on, opens. Any other shell can also be used.

2. Change to the location of the python program on the shell
	- write "cd C:\OBR_do_all_post_processing" on the shell and press ENTER.
		Now the shell is operating in the folder in which the python program is
		located.
		If the python program is saved at a different location, of course this 
		different location has to be stated.

3. Start the OBR-Do-all program
	- write "python OBR_do_all_post_processing.py" on the shell and press ENTER.
	- The OBR-Do-all program has started. 

4. Input the correct parameters for Filesorter program
	- Basically follow the instructions on screen. 
	- Input the location of the analyzed files.
		E.g. C:\Users\Username\Desktop\Sample_23017
	- Input the Base for the filename
		Input here everything right before the measurement number starts.
		If for example a typical filename is "2016-12-13_sample_23017_0023", 
		the "Base" of the filename is "2016-12-13_sample_23017_" (incl. 
		the "_" at the end).
	- Input the highest file-number.

5. Let the program create the correct folders and perform the noise reduction.

6. Check the noise reduced files for remaining outliers.
	- The program is NOT finished, but the user has most likely to do 
		some manual outlier correction.
	- Due to how the noise reduction algorithm works some outliers are 
		sometimes registered as real (false positives).
	- If one looks upon the PNG-files in the "PNG"-folder these remaining 
		outliers should easily be recognized.
	- Correct MANUALLY the files for which this is the case in the 
		"Noise_reduced_after_manual_correction"-folder.
	- ATTENTION: The very first file (0001_noise_reduced) is neither checked
		by the algorithm, nor present as PNG-file. So this file should be 
		checked by the user, too.

7. Let the program put the data into one (actually two) file
	- When finished just press ENTER and the program will put the
		data from many files into one file and the added up data from
		the many files into another file


Congratulations you have now two files which should be easy to import
into data visualization programs (like e.g. SciDAVIs). 
One file that contains all the NOT added up data from the many files: "0000_ALL_IN_ONE_NOT_ADDED_UP.txt", and another file that contains these 
values added up from measurement to measurement: "0000_ALL_ADDED_UP.txt"
The delimiter between the files is a tab.
These files can be found in the "Noise_reduced_after_manual_correction"-folder.









