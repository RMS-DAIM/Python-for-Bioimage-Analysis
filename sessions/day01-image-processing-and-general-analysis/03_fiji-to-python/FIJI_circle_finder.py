from ij import IJ #load the FIJI modules
from ij.io import FileSaver
from ij.io import OpenDialog
import os
from ij.measure import ResultsTable

IJ.run("Clear Results");  #clear results

od = OpenDialog("Choose a file", None)
filename = od.getFileName()
directory =  od.getDirectory()
path = od.getPath()

print filename
print directory
print path

imp = IJ.openImage(path)
imp.show()
#imp = IJ.getImage()
IJ.run("8-bit");
IJ.run("Invert");  #use this line if we need to invert the image
IJ.run("Set Measurements...", "area min redirect=None decimal=3");
IJ.run("Analyze Particles...", "display");

#save the results table as a CSV
#https://www.ini.uzh.ch/~acardona/fiji-tutorial/#s2
save_string = directory + 'Results_random_circles_CoronaTime.csv'
IJ.saveAs("Results", save_string);
#table = ResultsTable.getResultsTable()
