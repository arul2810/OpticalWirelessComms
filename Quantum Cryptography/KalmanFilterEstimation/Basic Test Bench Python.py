import numpy as np
import math
import tempfile
import sys

#sys.path.append('/Temp/PythonScripts/PythonSignalLibrary') #the directory that contains CDS_SystemManager
sys.path.append(tempfile.gettempdir() + '\OptiSystemTempDir')
#sys.path.append(tempfile.gettempdir() + '\OptiSystemTempDir\PythonSignalLibrary')
sys.path.append('C:\TEMP\PythonScripts\PythonSignalLibrary')


from SystemManager import *
from CalculationResult import *
from SignalLibrary import *