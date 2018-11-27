#=========================================================
# Header File
#=========================================================
""" 
SNAPHUNTER TOOL
header file
"""

# define authorship information
__authors__     = ['David Wong']
__author__      = ','.join(__authors__)
__credits__     = []
__copyright__   = 'Copyright (c) 2018'
__license__     = 'GPL'

# maintanence information
__maintainer__  = 'David Wong'
__email__       = 'david.agung.satrio@gmail.com'

#=========================================================
# Configuration
#=========================================================
import os
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import PyQt5.uic

#=========================================================
# Main Script
#=========================================================
class SnaphunterWindow(QtWidgets.QMainWindow):

    def __init__( self, parent = None ):
        """
        Snaphunter Window, put window from QMainWindow
        
        Keyword Arguments:
            parent {Object} -- parent from QMainWindow (default: {None})
        """
        
        super(SnaphunterWindow, self).__init__(parent)
        
        # load the ui
        basepath = os.path.dirname(__file__)
        basename = self.__class__.__name__.lower()
        uifile   = os.path.join(basepath, 'ui/{}.ui'.format(basename))
        PyQt5.uic.loadUi(uifile, self)
