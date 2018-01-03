# Manual for the OBR-Analyzer program
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

iv. The OBR program used to analyze the files was from Luna Technologies and 
simply called "Optical Backscatter Reflectometer", software version 3.12.2.
Throughout this document this program will be called "the OBR program"

v. The OBR_Noise_reducer.py program will be called "the python program" or
"the noise reducer" or something similar.

vi. For this document it is assumed that the python program 
(the OBR_Noise_reducer.py-file) is saved under "C:\OBR_Noise_reducer".
Of course it can be stored anywhere on the computer, the instructions given 
below must then just be adapted.

viii. The python program requires NO installation!

ix. It is assumed that the OBR_Filesorter.py program was used to sort the 
(raw) analysis files. This includes the creation of certain folders that are 
assumed to exist throughout this program. If not these folders need to be 
created as in the following example:
=> Assuming the files for an experiment are located e.g. under the parent 
directory
- C:\User\Username\Sample_23017
=> All analyzed files (all "_Lower"- and "_older_reference_Lower"-files)
need then to be in a subfolder to this directory called RAW (upper case!)
- C:\User\Username\Sample_23017\RAW
=> Three additional subfolders need to be created:
- C:\User\Username\Sample_23017\PNG
- C:\User\Username\Sample_23017\Noise_reduced_before_manual_correction
- C:\User\Username\Sample_23017\Noise_reduced_after_manual_correction

ATTENTION: The noise reducing program relies on this folder structure.

x. The python program is licensed under the GNU GPL version 3. This means 
that you as the user are allowed to change it according to your needs, without
asking for permission.
See http://www.gnu.org/licenses/ for more information.

This may be necessary for the maximum_difference_for_interpolation- and 
maximum_difference_between_points-parameters. See the source code of the 
noise reducing program for details.


## ## ## ## ## ## ## ## ## ## ## ## ##
Algorithm how to use the OBR_Noise_reducer-program.
## ## ## ## ## ## ## ## ## ## ## ## ##

0. Make sure the correct folder structure is present.
	- See point ix above.
	- If the OBR_Filesorter.py program was used everything is correct.

1. Open a command line interface
	- press and hold the <windows> button and press "R" (<windows-button> + R)
	- write "cmd" into the line in the small window that appears (without the 
		quotation marks). It will not be mentioned further that the quoation marks
		are not to be written, except when explicitely stated
	- The default windows command line interface, which will be called 
		"the shell" from now on, opens. Any other shell can also be used.

2. Change to the location of the python program on the shell
	- write "cd C:\OBR_Noise_reducer" on the shell and press ENTER.
		Now the shell is operating in the folder in which the python program is
		located.
		If the python program is saved at a different location, of course this 
		different location has to be stated.

3. Start the noise reducing program
	- write "python OBR_Noise_reducer.py" on the shell and press ENTER.
	- It may take a moment before all necessary modules are loaded.

6. Input the correct parameters for the noise reducing program
	- Basically follow the instructions on screen. 
	- Input the location of the raw analysis files.
		E.g. C:\User\Username\Sample_23017\RAW
	- Input the Base for the filename
		Input here everything right before the measurement number starts.
		If for example a typical filename is "2016-12-13_sample_23017_0023", 
		the "Base" of the filename is "2016-12-13_sample_23017_" (incl. 
		the "_" at the end).
	- Input the highest file-number.

7. Let the program reduce the noise in the files
	- Once you've input all parameters just press ENTER and the 
		python program starts the noise reducing algorithm and moves the
		files to the correct folders.
	- ATTENTION: If one (or several) parameters are wrong (e.g. too large
		highest file number or missing "_" in the base name) this will not be
		"discovered" by the program until it reaches this point and exits the
		program.
		Reading the error description may reveal which of the user input was 
		wrong.
		Simply run the noise reducer again with the correct parameters.


Congratulations your OBR an will have many OBR analysis files when the python program
is finished.









