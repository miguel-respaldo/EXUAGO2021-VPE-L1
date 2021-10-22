#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    This is the main File, where the algorythm works, to produce the output that
    the user wants. Here, the 3 modules created before do their work and finally
    give the user a new file in a specific format with the new information.
"""
#Import libraries and modules to the project
import sys
import argparse
import reading_file as rf
import translator as tr
import saving_file as sf

#Main function of the file.
def main():
    #This first part defines an object parser, and defines some of the arguments
    #that can receive, with their respective help text.
    parser = argparse.ArgumentParser(description='Compilator that translates\
            a given code and saves it into a .txt or .bin file.')

    parser.add_argument('file_name', type=str,
                        help='Name of the file that you want to translate.')
    parser.add_argument('-o', '--output-file', type=str, dest='ofile',
                        default='', required=False,
                        help='Creates the file with the given name.')
    parser.add_argument('-t', '--text', action='store_true', default=True,
                        dest='bool_t', required=False,
                        help='Sets the output file type as plane text.')
    parser.add_argument('-b', '--bin', action='store_true', default=False,
                        dest='bool_b', required=False,
                        help='Sets the output file type as a binary file.')
    args = parser.parse_args()

    #These conditionals sets the name of the new file and the type of it.
    if args.bool_b:
        ftype = '.bin'
    elif args.bool_t:
        ftype = '-bin.txt'
    if args.ofile != '':
        new_file = args.ofile
    else:
        #if the name has the original name, appends the extension ftype
        clean_name = args.file_name.split('.')
        new_file = clean_name
        if len(clean_name) > 1:
            new_file = clean_name[0]
        new_file += ftype

    #In this section, we call the functions that executes read, translation, and
    #write to the file in order to perform the translation.

    #We give the name of the file to the function that gets the information
    info = rf.readfile(args.file_name)

    #We call the translate function and we give it the list info that holds
    #the lines of code that the file had.
    binary = tr.translate(info)
    if binary == 0:
        sys.exit()
    #After the translation, we call the function that writes to the file, giving
    #it the name of the new file, a list with the binary code of the original
    #code, and the extension of the file
    sf.write_to(new_file, binary, ftype)

if __name__ == '__main__':
    main()
