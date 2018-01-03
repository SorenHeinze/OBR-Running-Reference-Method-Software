# Manual for the OBR-Buttonpresser program
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



How to use the OBR-Buttonpresser program


i. It is assumed that GNU/Linux users know their ways around basic procedures. 
So these instructions concentrate in some parts on windows users.

ii. This procedure was tested on a 64-bit, windows 7 Professional, Service pack 1.
operating system.

iii. It is assumed that python and all the necessary modules are installed. See 
the relevant document regarding this issue.

iv. The OBR program was from Luna Technologies and simply called 
"Optical Backscatter Reflectometer", software version 3.12.2.
Throughout this document this program will be called "the OBR program"

v. The OBR_buttonpresser_simple program will be called "the python program" or
"the (automated) buttonpresser" or something similar.

vi. For this document it is assumed that the python program 
(the OBR_buttonpresser_simple.py-file) is saved under "C:\OBR_buttonpresser".
Of course it can be stored anywhere on the computer, the instructions given 
below must then just be adapted.

vii. To clarify: all the measurements and saving of files is still done by the 
OBR program. The python program just presses the correct buttons at a given
time which allows automated experiments e.g. over night or several days.

viii. The python program requires NO installation!

ix. This version of the python program can be used just to measure one fibre.
If several fibres are used this program will NOT perform the switching 
between fibres.

x. ATTENTION: The automated measurement program takes over the mouse and keyboard 
of the computer it is running on. This means, this computer can not be used for
anything else. However, between automated actions enough windows occur in which 
nothing happens, so that the window that belongss to the automated measurement 
program can be closed. This will free the keyboard and mouse.

xi. The python program is licensed under the GNU GPL version 3. This means 
that you as the user are allowed to change it according to your needs, without
asking for permission.
See http://www.gnu.org/licenses/ for more information.


## ## ## ## ## ## ## ## ## ## ## ## ##
Algorithm how to use the OBR_buttonpresser_simple-program in connection 
with the above stated OBR measurement program.
## ## ## ## ## ## ## ## ## ## ## ## ##


1. Start and setup the OBR program
	- Perform one measurement and save this file at the same location where the 
		files during the automated measurements shall be saved.
	- The OBR program remembers the save location and the python program relies
		on that.
	- At a later stage the time for one measurement is needed as input parameter.
		it may be a good idea to stop the time for the first measurement so that
		this number is available.
	- It is recommended, albeit not necessary, to choose under 
		File => "Select File options" JUST the "Save Full Measurement File" option. 
		However, it IS important that the full measurement file is actually saved.
	- If after saving the first measurement a reference or another file is 
		loaded from a different location, the OBR program remembers this new 
		location and all measurements will be saved there (unless appropriate 
		actions are taken to avoid that).
	- A reference file from before the experiment should always be taken. 
		Thus everything done here is natural and done anyway.

1. Open a command line interface
	- press and hold the <windows> button and press "R" (<windows-button> + R)
	- write "cmd" into the line in the small window that appears (without the 
		quotation marks). It will not be mentioned further that the quoation marks
		are not to be written, except when explicitely stated
	- The default windows command line interface, which will be called 
		"the shell" from now on, opens. Any other shell can also be used.

2. Change to the location of the python program on the shell
	- write "cd C:\OBR_buttonpresser" on the shell and press ENTER.
		Now the shell is operating in the folder in which the python program is
		located.
		If the python program is saved at a different location, of course this 
		different location has to be stated.

3. Start the automated OBR measurements program
	- write "python OBR_buttonpresser_simple.py" on the shell and press ENTER.
	- The automated OBR measurements program has started. 
	
	- Move the shell-window to a position at which it does NOT obstruct
		the <SCAN> Button of the OBR program!

4. Input the correct parameters for the automated OBR measurements program
	- Basically follow the instructions on screen. 
	- Input how many measurements shall be taken
	- Input the time that is needed for ONE measurement. This was mentioned
		already under 1.
		ATTENTION: It was observed that measurements sometimes need longer.
		The python program tries to take such eventualities into account by adding
		ten more seconds to the number you state here.
	- Input the time between measurements.
		ATTENTION: This time must be greater then the time for one measurement PLUS
		23 seconds. This is because it was often observed that the OBR program is 
		lagging behind the python program and thus the latter stops working properly.
		To adjust for this breaks are build into the python program.
		ATTENTION: DON'T adjust the time between measurements for the time the 
		actual measurement needs! This is done by the python program.
		For example if the time between measurements is 900 seconds and one 
		measurement needs 51 seconds (incl. everything the python program does 
		internally), then the measurement will be performed and the next 
		measurement will be started after 900 - 51 = 949 seconds.
	- Input the Base for the filename
		The files are numbered consecutively. 
		If nothing is stated here the files will have filenames like
		"0001", "0002", ... "0251" etc.
		However, may be advantageous to state here e.g. the date or the sample 
		number (for example "2016-12-13_sample_23017_")

5. Tell the python program where the <SCAN> Button is.
	- If not already done, move the shell-window to a position at which it does 
		NOT obstruct the <SCAN> Button of the OBR program!
	- Follow the instructions given in the shell-window.
		Move the mouse pointer over the <SCAN> button 
		DON'T click the mouse because this will set the OBR program window
		as the active window!
		Don't move the mouse away from the <SCAN> button and press ENTER on 
		the shell.
	- The python program detects now the position of the pointer and will 
		click at this position for all automatic measurements

ATTENTION: DON'T MOVE THE OBR PROGRAM WINDOW BECAUSE BEYOND THIS POINT 
			BECAUSE THIS WILL CHANGE THE POSITION OF THE <SCAN> BUTTON!

6. Start the automated measurements
	- After the <SCAN> Button is detected, just press ENTER on the shell.
	- The OBR program will become the active window, but the python program
		will continue to run in the background. The shell must not be the
		active window for this.


Congratulations you will have many OBR measurement files when your experiment 
is finished.









