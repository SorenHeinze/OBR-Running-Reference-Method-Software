#    "OBR_add_up_data" (v1.0)
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


# This program adds up strain data from consecutive OBR measurements.
# It takes in files that contain JUST the table with the data as produced by
# OBR_Noise_reducer.py.
# 
import os

# Just a function that puts zeros in front of numbers. I wrote this before
# I've learned about .zfill().
def make_number(i):
	if i < 10:
		return '000%s' % i
	elif i < 100:
		return '00%s' % i
	elif i < 1000:
		return '0%s' % i

# This function will executed when this program is called on the console.
# I don't like this spaghetti code herein, but well, this is a too short 
# program for restructuring everything.
# 
# # That I can call main() from other modules with the correct parameters 
# I decided to have file_folder as parameter.
# 
# To have this however also as a standalone program, I ask for this
# parameter in the if-construct that is called when this program is called
# on the shell.
def main(file_folder):
	all_files_sorted = sorted(os.listdir(file_folder))

	# To get the correct delimiter in a filename I have to do this so that it 
	# is done the correct way under windows.
	first_infile = os.path.join(file_folder, all_files_sorted[0])

	# Number of noise reduced files.
	number_of_files = len(all_files_sorted)

	# Number of lines with data in the noise reduced files.
	linecount = 0
	with open(first_infile, 'r') as f:
		for line in f:
			linecount += 1

	# I've made the observation that some files miss one line in the end.
	# This would mess up the remainder of the program, so I compensate for this,
	number_of_lines = linecount - 1

	# The dict that will contain the x-values as keys and all the y-values to each 
	# x-value.
	values = {}
	# This list contains all the x-values (in the correct order) which are 
	# supposed to be the same for all measurements.
	x_values = []

	# I need to get the x-values.
	with open(first_infile, 'r') as f:
		for line in f:
			# I don't remember why I have a try-except statement here.
			# It probably is unnecessary, but it seems to help with finding 
			# errors in the files.
			try:
				x_value = float(line.split('\t')[0])
			except ValueError:
				print f, line
				break

			x_values.append(x_value)

	# Create the lists for the separate y-values for each measurement to the 
	# (similar) x-values.
	# This will be for the file that contains all values NOT added up.
	for value in x_values:
		values[value] = []

	# Read each file, get the second value in the table and add it
	# to the dict
	for i in range(0, number_of_files):
		infile_addendum = '%s_noise_reduced.txt' % (make_number(i + 1))
		infile = os.path.join(file_folder, infile_addendum)

		with open(infile, 'r') as f:
			j = 0
			for line in f:
				if j < number_of_lines:
					value = float(line.split('\t')[1])
					values[x_values[j]].append(value)
					j += 1

	# Write these values into the file that contains the NOT added up data.
	# A tab shall be the separator the x-value shall be leftmost and all y-values 
	# to the right of it.
	not_added_up_outfile = os.path.join(file_folder, '0000_ALL_IN_ONE_NOT_ADDED_UP.txt')
	with open(not_added_up_outfile, 'w') as f:
		for x_value in x_values:
			f.write('%s\t' % x_value)
			y_values = values[x_value]
			for y_value in y_values:
				f.write('%s\t' % y_value)
			f.write('\n')


	# Now do the same more or less again, for the file that shall contain all
	# the values added up.
	# 
	# I don't need to get the x-values again. But I need to start with a fresh dict.
	values = {}
	for value in x_values:
		values[value] = []

	for i in range(0, number_of_files):
		infile_addendum = '%s_noise_reduced.txt' % (make_number(i+1))
		infile = os.path.join(file_folder, infile_addendum)
		with open(infile, 'r') as f:
			# The first file can not add up anything.
			if i != 0:
				print "Adding up data for file", i
				j = 0
				for line in f:
					if j < number_of_lines:
						# If the index is "-1" the very last member of this list
						# will be used
						value = float(line.split('\t')[1]) + values[x_values[j]][-1]
						values[x_values[j]].append(value)
						j += 1
			# The else-case is just for the very first file, because I need to have
			# sth. that I can add up for the remaining files.
			else:
				j = 0
				for line in f:
					if j < number_of_lines:
						value = float(line.split('\t')[1])
						values[x_values[j]].append(value)
						j += 1

	added_up_outfile = os.path.join(file_folder, '0000_ALL_ADDED_UP.txt')
	with open(added_up_outfile, 'w') as f:
		for x_value in x_values:
			f.write('%s\t' % x_value)
			y_values = values[x_value]
			for y_value in y_values:
				f.write('%s\t' % y_value)
			f.write('\n')


	print """\n
You will find the two files for easy import into data visualization programs
in %s .
""" % file_folder



# When this program is called on the console, main() is executed.
# See comment to main() why I do here more then just executing main().
if __name__ == '__main__':
	print """
ATTETNION: Have you checked the very first file for outliers? 
This was NOT done by the noise reducing program even though the filename says so!
"""
	# Just to give the user a chance to check that. It does not really matter
	# what the user tells me here :P .
	raw_input("y/n: ")

	file_folder = raw_input("\nFolder that contains the (noise reduced) files: ")

	# ATTENTION: This program relies upon that JUST noise reduced files are in 
	# this folder
	print "\nMake sure that JUST noise reduced files are in the folder"
	raw_input("Is this the case (y/n): ")

	main(file_folder)









