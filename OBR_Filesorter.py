#    "OBR_Filesorter" (v1.0)
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


# A small program to automatically sort all the analyzied files that were 
# created during the automameted analysis of OBR measurements using the
# OBR_analyzer_simple.py program.
# 
# This program assumes that the running reference method was used to analyze
# the OBR-measurement files. This means that two "property of interest" 
# (e.g. strain or temperature) files exist, one of these labeled with 
# "_older_referencere" at the end of the filename.
# Also it is assumed that the amplitude files were stored with the keyword 
# "_Upper" and that the files with the property of interest have the 
# keyword "_Lower" at the end of the filename.
# 
# This is the case for a certain version of the proprietary 
# OBR-measurement/analyzing program (stated in the accompanying manual to this
# program) and the OBR_analyzer_simple.py program were used.
# 
# This program creates some folders and moves the files, according to the 
# keywords into those folders for later, subsequent human inspection of 
# the data.
#
# I decided to restrict myself to the most basic programming statements 
# (if possible) and NOT to use functions or classes. 
# While I personally don't like this, I hope that this makes it easier for 
# the interested but usually not programming user when she or he does not need 
# to jump to different places or even files while trying to understand what's
# going on here.
# 
# 
# ATTENTION: The file in which all the analysis files are located must be 
# stated as all_files_directory to make this program work.

import os
# shutil is here for using the correct operative specific move commands.
import shutil


# This function will executed when this program is called on the console.
# I don't like this spaghetti code herein, but well, this is a too short 
# program for restructuring everything.
# 
# # That I can call main() from other modules with the correct parameters 
# I decided to have all_files_directory as parameter.
# 
# To have this however also as a standalone program, I ask for this 
# parameter in the if-construct that is called when this program is called
# on the shell.
def main(all_files_directory):
	# Create the path's for the folders to be created.
	# 
	# Not all operative systems use the same delimiters in the path-name.
	# os.path.join() takes care of that.
	raw_folder = os.path.join(all_files_directory, 'RAW')
	amplitude_files_folder = os.path.join(raw_folder, 'Amplitude_files') 
	png_folder = os.path.join(all_files_directory, 'PNG') 
	before_manual_correction_folder = os.path.join(all_files_directory, \
											'Noise_reduced_before_manual_correction')
	after_manual_correction_folder = os.path.join(all_files_directory, \
											'Noise_reduced_after_manual_correction') 

	# Create the folders
	os.system('mkdir "%s"' % raw_folder)
	os.system('mkdir "%s"' % amplitude_files_folder)
	os.system('mkdir "%s"' % png_folder)
	os.system('mkdir "%s"' % before_manual_correction_folder)
	os.system('mkdir "%s"' % after_manual_correction_folder)


	all_sorted_filenames = sorted(os.listdir(all_files_directory))

	# Sort all files into the correct folders.
	for filename in all_sorted_filenames:
		# If OBR_analyzer_simple is used two identical "_Upper"-files
		# exists just with different names. One of these is to be deleted ...
		if '_Upper' in filename and '_older_reference' in filename:
			remove_this = os.path.join(all_files_directory, filename)
			os.remove(remove_this)
		# ... the other one is to be moved to the correct folder.
		elif '_Upper' in filename:
			from_here = os.path.join(all_files_directory, filename)
			to_there = os.path.join(amplitude_files_folder, filename)
			shutil.move(from_here, to_there)
		# The "_Lower"-files contain the property of interest and are to be moved
		# to the RAW-folder.
		elif '_Lower' in filename:
			from_here = os.path.join(all_files_directory, filename)
			to_there = os.path.join(raw_folder, filename)
			shutil.move(from_here, to_there)





# When this program is called on the console, main() is executed.
# See comment to main() why I do here more then just executing main().
if __name__ == '__main__':
	# Get the location of the raw analyzed files
	all_files_directory = raw_input('Raw analysis files location (e.g. C:\OBR\Sample_23): ')

	main(all_files_directory)










