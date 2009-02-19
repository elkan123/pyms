"""
Classes used for the manipulation of mass spectral libraries
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

from pyms.libMS.JCAMP.IO import load_jcamp

class MSLib(object):

    """
    @summary: Models a MS library

    @author: Qiao Wang
    @author: Vladimir Likic
    """

    def __init__(self, file_name, format="JCAMP"):

        """
        @summary: Initialize the library

        @para file_name: The input jcamp file name
        @type file_name: StringType
        @para format: Format of the input library file. Currently
            only "JCAMP" allowed
        @type format: String

        @author: Qiao Wang
        @author: Vladimir Likic
        """

        if format == "JCAMP":
            self.records = load_jcamp(file_name)
        else:
            error("unknown mass spec library format")

    def printl(self, begin=1, end=None):

        """
        @summary: Print the records in memmory

        @para begin: The start record
        @type begin: IntType
        @para end: The end record
        @type end: IntType

        @author: Qiao Wang
        @author: Vladimir Likic
        """

        if end == None:
            end = len(self.records)

        if end <= len(self.records):
            for ii in range(begin-1,end):
                record = self.records[ii]
                print "(%d)" % ( ii+1 ),
                print record.name
                for item in record.mass_record:
                    print "\t", item
        else:
            print "Out of the boundary, retry"

class MSLibRecord(object):

    """
    @summary: Models a MS libarary Record

    @author: Qiao Wang
    @author: Vladimir Likic
    """

    def __init__(self, name, mass_record):

        """
        @summary: Initialize the record

        @para name: The compound name
        @type name: StringType
        @para mass_record: The list mass spectrum values
        @type mass_record: ListType

        @author: Qiao Wang
        @author: Vladimir Likic
        """

        self.name = name
        self.mass_record = mass_record


class MatchObj(object):

    """
    @summary: Models mass spectral library matching record

    @author: Qiao Wang
    @author: Vladimir Likic
    """

    def __init__(self, cmpd_name, mass_record, score):

        """
        """

        self.id = cmpd_name
        self.mass_record = mass_record
        self.score = score
