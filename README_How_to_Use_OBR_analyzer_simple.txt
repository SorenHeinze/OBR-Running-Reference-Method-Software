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

iv. The OBR program was from Luna Technologies and simply called 
"Optical Backscatter Reflectometer", software version 3.12.2.
Throughout this document this program will be called "the OBR program"

v. The OBR_analyzer_simple.py program will be called "the python program" or
"the (automated) analyzer" or something similar.

vi. For this document it is assumed that the python program 
(the OBR_analyzer_simple.py-file) is saved under "C:\OBR_analyzer".
Of course it can be stored anywhere on the computer, the instructions given 
below must then just be adapted.

vii. To clarify: all the analysis and saving of files is still done by the 
OBR program. The python program just presses the correct buttons at a given
time which allows automated analyses e.g. over night.

viii. The python program requires NO installation!

ix. It is assumed that the OBR measurement files all have the same filename
except for a running number in the end. This running number must have four 
leading zeros.
This will be the case if the OBR_buttonpresser_simple.py program
was used for automated measurements.

x. This version of the python program can be used just for the so called
running reference method. In this method a OBR measurement file is analyzed twice.
Once with the second to last measurement as a reference file, and once with the 
last measurement as a reference file.
Of course this is not possible for the very first measurement (counting the 
reference file from before the measurement as zero). This case will be covered
below in detail.

xi. The analyzed files will be stored in the same folder as the measurement files.

xii. ATTENTION: The automated analysis program takes over the mouse and keyboard 
of the computer it is running on. This means, this computer can not be used for
anything else. However, between automated actions enough windows occur in which 
nothing happens, so that the window that belongss to the automated measurement 
program can be closed. This will free the keyboard and mouse.

xiii. The python program is licensed under the GNU GPL version 3. This means 
that you as the user are allowed to change it according to your needs, without
asking for permission.
See http://www.gnu.org/licenses/ for more information.


## ## ## ## ## ## ## ## ## ## ## ## ##
Algorithm how to use the OBR_analyzer_simple-program in connection 
with the above stated OBR measurement/analyzer program.
## ## ## ## ## ## ## ## ## ## ## ## ##

1. Start and setup the OBR program
	- Set the reference file from before the measurement started.
		"File" => "Load Reference File"
	- Load the first measurement file.
	- Make sure that under "Options" => "Sensing" the "Sensing Enabled" option
		is activated.
	- Choose in the lower window the property you want to be analyzed.
	- Find the area along the fibre in which the analysis shall take place and
		set up the parameters for the virtual strain gauges.
	- Before saving it is recommended, to choose under File => "Select File options" 
		the following options:
		=> "Save File for Upper graph" (Amplitude (dB))
		=> "Save File for Lower Graph" (the property you are interested in)
		It is recommended NOT to save several properties (e.g Temperature Change 
		+ Strain) into one file. This will interfere with other programs in this
		series of "automated OBR data handling"-programs.
		It is recommended to uncheck the "Save Full Measurement File" option.
		However, this is not necessary.
	- Save this analysis under the same name as the name of this first 
		measurement file (e.g. "Sample_23017_0001").
		The OBR program takes care of the correct labeling of upper and lower
		graph files.
	- At a later stage the time how long it takes to save is needed as input 
		parameter. It may be a good idea to stop the time for the saving while
		you are at it anyway.

2. Figure out the time it takes to analyze a measurement.
	- At a later stage the time how long it takes to analyze a measurement is 
		needed as input parameter. 
		This is a very important parameter to exclude errors during the 
		automated analysis that may occur because an analysis takes more time
		than anticipated.
		This time is heavily influenced by how many outliers or noise are/is 
		in the data. Since much noise is expected it is recommended here to do 
		the following to determine this time.
		It is assumed that all the steps in point 1. were followed; so the 
		reference file is loaded and the virtual strain gauge parameters are set.
	- Load a totally different measurement file that has nothing to do with 
		this experiment. 
		Since there is no connection whatsoever with the loaded reference file
		this is like analyzing pure noise and the analysis will take a maximum 
		amount of time.
	- Right after pressing the "OK" Button in the "Load File" menu start 
		counting the seconds until no "Processing" popup-window can be seen 
		any longer. This window should pop up twice. Sometimes however one of 
		these popup windows disappears very fast.
	- Since another file was loaded the OBR program now remembers the wrong 
		file location.
		Hence, load again the correct first measurement file of the experiment 
		you actually want to analyze. It is not necessary to save this 
		again, if this was already done under point 1.

3. Open a command line interface
	- press and hold the <windows> button and press "R" (<windows-button> + R)
	- write "cmd" into the line in the small window that appears (without the 
		quotation marks). It will not be mentioned further that the quoation marks
		are not to be written, except when explicitely stated
	- The default windows command line interface, which will be called 
		"the shell" from now on, opens. Any other shell can also be used.

4. Change to the location of the python program on the shell
	- write "cd C:\OBR_analyzer" on the shell and press ENTER.
		Now the shell is operating in the folder in which the python program is
		located.
		If the python program is saved at a different location, of course this 
		different location has to be stated.

5. Start the automated OBR analysis program
	- write "python OBR_analyzer_simple.py" on the shell and press ENTER.
	- The automated OBR analysis program has started. 
	- Move the shell-window to a position at which it does NOT obstruct
		the <FILE> Button of the OBR program and also not a space of ca. 
		100 pixel below this button.

6. Input the correct parameters for the automated OBR analysis program
	- Basically follow the instructions on screen. 
	- Input the number of the last measurement file.
	- Input the number of the first file to be analyzed.
		This is usually "2" but can be different if e.g. if the automated 
		analysis is interrupted and one wants to continue from this point.
	- Input the time for ONE analysis
		This is a very important parameter because it determines how long 
		the automated analyzer program waits for the OBR program to be 
		finished before it attempts to e.g. change the reference or save the 
		files.
		See point 2 for more information. 
		ATTENTION: It was observed that an analysis sometimes need much longer
		than anticipated.
		The python program tries to take such eventualities into account by adding
		ten more seconds to the number you state here.
	- Input the time it takes to save the files.
		At fast computers this is usually NOT an issue. However, at slow 
		computers this may take up to a couple of seconds and the automated
		analysis program has to wait before it can continue.
		ATTENTION: It was observed that an analysis sometimes need much longer
		than anticipated.
		The python program tries to take such eventualities into account by adding
		five more seconds to the number you state here.
	- Input the Base for the filename
		Input here everything reight before the number starts.
		If for example a typical filename is "2016-12-13_sample_23017_0023", 
		this "Base" of the filename is "2016-12-13_sample_23017_" (incl. 
		the "_" at the end).

7. Tell the python program where the <FILE> Button is.
	- If not already done, move the shell-window to a position at which it does 
		NOT obstruct the <FILE> Button of the OBR program and also not a 
		space of ca. 100 pixel below this button.!
	- Follow the instructions given in the shell-window.
		Move the mouse pointer over the <FILE> button 
		DON'T click the mouse because this will set the OBR program window
		as the active window!
		Don't move the mouse away from the <FILE> button and press ENTER on 
		the shell.
	- The python program detects now the position of the pointer and will 
		click at this position for all automatic analysis'.

ATTENTION: DON'T MOVE THE OBR PROGRAM WINDOW BECAUSE BEYOND THIS POINT 
			BECAUSE THIS WILL CHANGE THE POSITION OF THE <SCAN> BUTTON!

8. Start the automated analysis 
	- After the <FILE> Button is detected, just press ENTER on the shell.
	- The OBR program will become the active window, but the python program
		will continue to run in the background. The shell must not be the
		active window for this.


Congratulations you will have many OBR analysis files when the python program
is finished.









