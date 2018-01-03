#    "OBR_do_all_post_processing" (v1.0)
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


# This program calls just OBR_Filesorter, OBR_Noise_reducer and OBR_add_up_data
# so that the user does not need to call these separately.
# 
# See the source of these programs what assumptions were made for proper
# execution of these programs.

print "Loading modules (this may take some seconds) ..."

from copy import deepcopy
import matplotlib.pyplot as plt
import os
# shutil is here for using the correct operative specific move commands.
import shutil
import OBR_Filesorter as fs
import OBR_Noise_reducer as nr
import OBR_add_up_data as aud

all_files_directory = raw_input('\nRaw analysis files location (e.g. C:\OBR\Sample_23): ')
name_base = raw_input('Analysis files name base (e.g. 2016-12-13_sample_23017_): ')
maximum_number = int(raw_input('Highest file number: '))

# OBR_Filesorter creates folders and moves the raw analysed files to
# the RAW-folder.
fs.main(all_files_directory)

# OBR_Noise_reducer works on the RAW-folder, hence I need to get this
# as a parameter.
raw_folder = os.path.join(all_files_directory, 'RAW')

nr.main(raw_folder, name_base, maximum_number)

noise_reduced_folder = os.path.join(all_files_directory, \
									'Noise_reduced_after_manual_correction')

print """
\nCheck for outliers that the automatic algorithm "overlooked". 

If necessary correct manually the files in %s .
Don't forget to also check the very first file ("0001_noise_reduced").

When this is done come back to this console and press ENTER, the program
will continue automatically.

ATTENTION: DON'T MOVE THE FILES TO DIFFERENT FOLDERS!!!

""" % noise_reduced_folder

raw_input("Manual correction for outliers finished (y/n): ")

aud.main(noise_reduced_folder)









