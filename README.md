# OBR-Running-Reference-Method-Software

## Description
Software used in a research project using an  Optical Backscatter Reflectometer (OBR) to obtain strain data of curing epoxy

This software is meant for re-use in similar projects. Hence, it is not written for more general purpose.

Three main software-packages are to be considered. Software for
i) the (semi) automatic measurements
ii) the (semi) automatic strain analysis of the raw data, yielding the strain-data-files.
iii) post-analysis, yielding the (automatic) noise reduced strain-data files.

The programs are written in Python 2.7 and a detailed instruction how to install python and the necessary modules can be found in the repository.

The software is NOT meant to be installed but rather to be run from a command line.

The source code for all programs is extensively commented for easy user adjustments.

i) and ii) are auto-clickers that are more or less useful just in connection with the proprieatry OBR 4600 Software from Luna.
=> "(semi) automatic" means that some input is required for these programs to work.

The python source-files for OBR_Noise_reducer, OBR_Filesorter, OBR_add_up_data and OBR_do_all should be the same as in the parent folder.

## Usage
Put all .py-files into one folder and simply run the programs in a command line window. Remember, that python 2.7 was used to write the software.

For less experienced users detailed step-by-step instruction how to use each program under windows-OS are provided.
