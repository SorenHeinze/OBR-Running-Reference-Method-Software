#    "OBR_buttonpresser_simple" (v1.0)
#    Copyright 2016 Soren Heinze
#    soerenheinze <at> gmx <dot> de
#    5B1C 1897 560A EF50 F1EB 2579 2297 FAE4 D9B5 2A35
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


# A small program to automatically press the "Scan"-button of a proprietary
# OBR-measurement program.
# The files will also be saved automatically, assuming that CTRL + S 
# is the shortcut to open the "save-file" dialogue of OBR-measurement program.
# 
#
# I decided to restrict myself to the most basic programming statements 
# (if possible) and NOT to use functions or classes. 
# While I personally don't like this, I hope that this makes it easier for 
# the interested but usually not programming user when she or he does not need 
# to jump to different places or even files while trying to understand what's
# going on here.

from pymouse import PyMouse
from pykeyboard import PyKeyboard
from time import sleep, time


# Instantiate a mouse and a keyboard.
# A PyMouse() and a PyKeyboard() have certain methods that allow 
# easy access to typical features of such peripherals like moving the
# pointer to a certain position or pressing keyboard buttons.
mouse = PyMouse()
keyboard = PyKeyboard()


# Just reminding the user of sth. very important.
print '''\n\n
ATTENTION:
DON'T MOVE THE WINDOW OF THE OBR-PROGRAM, AFTER THE POSITION OF THE <SCAN> BUTTON
WAS DETERMINED!

See the instructions that accompany this program, how to use it.\n
'''


# Don't do more measurements than the number stated here.
# 
# Users tend to make mistakes. E.g. pressing too fast ENTER before 
# actually entering a number.
# I catch the most common mistakes by using the while-loop, the try-except
# statement and by trying to convert to a number at once.
correct_input = False
# Continue until the input given by the user is a number.
while not correct_input:
	# Try to do sth. specific ...
	try:
		# Get the input from the user. If raw_input() contains a string
		# between the brackets, this string will be printed on the 
		# shell to give the user some more information.
		input_from_user = raw_input('Number of Measurements: ')
		# raw_input() returns a string. But a number is required. Hence I
		# convert the string to a number.
		# 
		# These two statements are summed up into one line in the while-loops
		# below.
		stop_here = int(input_from_user)
		# If everything is correct, set correct_input to True, which means
		# that the while-loop will NOT start again.
		correct_input = True
	# ... unless the user gives wrong input. ...
	except ValueError:
		# ... If this is the case case just ignore it and start the loop
		# again.
		pass


# Reset correct_input for the next user-input.
correct_input = False


# The time one measurement takes
while not correct_input:
	try:
		measurement_time = int(raw_input('Time for ONE measurements in full SECONDS: '))
		correct_input = True
	except ValueError:
		pass

# I've observed that measurements sometimes need more time then anticipated.
# Here I try to compensate a bit for such cases.
measurement_time += 10


correct_input = False


message_3 = 'Time between measurements in full SECONDS. Must be greater then '
message_4 = 'time for ONE measurements + 23 seconds! : '
# The time between measurements. 
while not correct_input:
	try:
		pause_intervall = int(raw_input(message_3 + message_4))
		correct_input = True
	except ValueError:
		pass


# The base-filename. e.g. 2017-05-23_Sample_E23_"
# The name will be "filled up" by the measurement-number in the 
# measurement-loop below.
base_filename = raw_input('"Base" for filenames (e.g. "Sample_01_") ')


# A visual separator to make the use of this program easier for the user.
print "\n\n<<<<<<<< Basic user input complete >>>>>>>>"


# Instructions for the user what to do, so that the program can determine the 
# position of the <SCAN> Button
print """\n
Move the mouse pointer over the <SCAN> Button of the OBR program.

DON'T click the mouse! 
The console must remain the active window!

Once this is done, press ENTER (the position of the <SCAN> Button will
be detected).

DON'T MOVE THE WINDOW OF THE OBR-PROGRAM AFTERWARDS!\n
"""


# Using raw_input() I make sure that the program will halt here and wait 
# for ENTER.
raw_input('Press ENTER when the mouse is over the <SCAN> Button.')


print "\n\n<<<<<<<< <SCAN> Button position determined >>>>>>>>"


# Here the position of the mouse pointer is determined.
# .position() returns a tuple that contains the x- and y-coordinates
# of the pointer at the time this method is called.
button_position = mouse.position()


# Some more information for the user.
print """\n
ATTENTION: DON'T MOVE THE WINDOW OF THE OBR-PROGRAM

After pressing ENTER again the OBR window will become active and the 
automatic measurements will start.
DON'T make this console the active window after pressing ENTER.
It will work even if you can't see this console.\n
"""


# Wait here for the user to start the automatic measurements.
raw_input('Press ENTER now to start the automatic measurements. >>>')


# Give the user a summary of the input information.
print "\n-----------------------\n"
print "ATTENTION: DON'T MOVE THE WINDOW OF THE OBR-PROGRAM!\n"
print "Automated Measurements have started.\n"
print "Number of Measurements: %s" % stop_here
print "Time for ONE measurement: %s seconds" % measurement_time - 10
print "Time between measurements: %s seconds" % pause_intervall
print "Base-filename: %s" % base_filename
print "\n-----------------------\n"





## ## ## ## ## Here the measurement-loop starts ## ## ## ## ##





# This counter counts the number of measurements already performed.
counter = 0

while counter < stop_here:
	# Record the time when the loop starts to determine how much time 
	# the whole loop took and subtract this from the pause intervall
	# between the measurements.
	start_time = time()

	# Increase the measurement-counter
	counter += 1

	# Some operating systems order files wrong. I will not go into 
	# detail about this issue here because it is easily solved by putting
	# leading zeros in front of the number.
	# This is done by .zfill(). However, .zfill() can be used just on 
	# a string, but the counter is a number. Thus I first convert the number 
	# to a string.
	file_number = str(counter).zfill(4)
	# Make the correct filename, by concatenating the base-filename and
	# the number for the measurement that is performed.
	filename = base_filename + file_number

	# .click(X, Y) moves the mouse to position (X, Y) and clicks there
	# once.
	mouse.click(button_position[0], button_position[1])

	# I put in sleep() statements all over this loop to give the 
	# measurement-PC some time to "settle" between commands.
	sleep(0.5)
	# I've observed that sometimes a click is not registered by 
	# the measurement-computer. To compensate for that I just click again.
	# If the <SCAN> Button was clicked already the first time, it doesn't
	# matter since a measurement takes more time then the 0.5 seconds
	# between these two clicks.
	# button_position[0] / button_position[1] retrieves the first / second 
	# entry of the tuple that contains the x- and y-coordinates of the 
	# <SCAN> Button. See also comment above.
	mouse.click(button_position[0], button_position[1])

	# Wait out until the measurement is finished.
	print "Waiting for the measurement to be finished ..."
	sleep(measurement_time)

	# Open the "Save File"-screen.
	# .press_key() is a method of a PyKeyboard-instance that presses and holds
	# the given key and does NOT release it until release_key() is called.
	# keyboard.control_l_key selects the left CTRL-key
	keyboard.press_key(keyboard.control_l_key)
	# .tap_key() taps the given key.
	keyboard.tap_key('s')
	# Don't forget to release the pressed CTR-key.
	keyboard.release_key(keyboard.control_l_key)

	# Just to make sure that the save-file screen can be seen.
	sleep(2)

	# Input the filename.
	keyboard.type_string(filename)
	sleep(1)

	# And press ENTER so that the OBR measurement program will save the file.
	keyboard.tap_key(keyboard.return_key)

	# Calculate how much time this whole process took.
	end_time = time()
	# loop_time will be in seconds.
	loop_time = end_time - start_time

	time_to_next_measurement = pause_intervall - loop_time
	
	message_5 = 'Performed measurement %s. ' % counter
	message_6 = 'Next measurement in %s seconds.'  % int(time_to_next_measurement)
	print message_5 + message_6

	# Don't do anything until the next measurement has to be performed. 
	# Then start the measurement-loop again.
	sleep(time_to_next_measurement)









