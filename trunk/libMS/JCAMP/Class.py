"""
Classes used for the manipulation of mass spectral libraries in JCAMP format
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


class MSLibRecord(object):

    """
    @summary: Models a MS libarary Record

    @author: Qiao Wang
    @author: Vladimir Likic
    """

    def __init__(self, name, mass_spectrum):

        """
        @summary: Initialize the record

        @para name: The compound name
        @type name: StringType
        @para mass_spectrum: The list mass spectrum values
        @type mass_spectrum: ListType

        @author: Qiao Wang
        @author: Vladimir Likic
        """

        self.name = name
        self.mass_spectrum = mass_spectrum

