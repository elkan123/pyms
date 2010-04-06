"""
Provides helper functions for MID processing
"""

 #############################################################################
 #                                                                           #
 #    PyMS software for processing of metabolomic mass-spectrometry data     #
 #    Copyright (C) 2005-8 Vladimir Likic                                    #
 #                                                                           #
 #    This program is free software; you can redistribute it and/or modify   #
 #    it under the terms of the GNU General Public License version 2 as      #
 #    published by the Free Software Foundation.                             #
 #                                                                           #
 #    This program is distributed in the hope that it will be useful,        #
 #    but WITHOUT ANY WARRANTY; without even the implied warranty of         #
 #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
 #    GNU General Public License for more details.                           #
 #                                                                           #
 #    You should have received a copy of the GNU General Public License      #
 #    along with this program; if not, write to the Free Software            #
 #    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.              #
 #                                                                           #
 #############################################################################

from pyms.Utils.Error import error
from pyms.MIDs.Class import MID
from pyms.Utils.IO import file_lines
from pyms.Utils.Time import time_str_secs

def parse_ion_defs(in_file):

    """
    @summary:

    @param in_file:
    @type in_file: StringType

    @return: the list of ...
    @rtype: ListType

    @author: Milica Ng
    @author: Vladimir Likic
    """

    lines = file_lines(in_file, filter=True)
    mids_list = []

    for line in lines:

        # parse input lines
        items = line.split(',')

        # each MID specification must have exactly 4 elements
        if len(items) != 4:
            print "\n Input file: ", in_file
            print " Line: ", line
            error("A MID specification must have exactly 4 elements")

        metabolite_name = items[0]
        rt = time_str_secs(items[1]) # convert to seconds
        diagnostic_ion = int(items[2])
        mid_size = int(items[3])

        # set compound name, retention time, diagnostic ions and MID size
        mids = MID(metabolite_name, rt, diagnostic_ion, mid_size)

        # store mids in mids_list
        mids_list.append(mids)

    return mids_list

def parse_data_defs(in_file):

    """
    @summary:

    @param in_file:
    @type in_file: StringType

    @return: the list of ...
    @rtype: ListType

    @author: Milica Ng
    @author: Vladimir Likic
    """

    lines = file_lines(in_file, filter=True)

    data_files = []  
    for line in lines:
        data_files.append(line)

    return data_files
