"""
Top-hat baseline corrector
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

import copy
import numpy
from scipy import ndimage

from pyms.IO.Utils import is_ionchromatogram, ic_window_points

# default structural element as a fraction of total number of points
_STRUCT_ELM_FRAC = 0.2

def tophat(ic, struct=None):

    """
    @summary: Top-hat baseline correction

    @param ic: The input ion chromatogram
    @type ic: pyms.IO.Class.IonChromatogram
    @param struct: Top-hat structural element as time string
    @type struct: StringType

    @return: Top-hat corrected ion chromatogram
    @rtype:  pyms.IO.Class.IonChromatogram

    @author: Woon Wai Keen
    @author: Vladimir Likic
    """

    if not is_ionchromatogram(ic):
        error("'ic' not an IonChromatogram object")
    else:
        ia = copy.deepcopy(ic.get_intensity_array())

    if struct == None:
        struct_pts = int(round(ia.size * _STRUCT_ELM_FRAC))
    else:
        struct_pts = ic_window_points(ic,struct)

    print " -> Top-hat: structural element is %d point(s)" % ( struct_pts )

    str_el = numpy.repeat([1], struct_pts)
    ia = ndimage.white_tophat(ia, None, str_el)

    ic_bc = copy.deepcopy(ic)
    ic_bc.set_intensity_array(ia)

    return ic_bc 
