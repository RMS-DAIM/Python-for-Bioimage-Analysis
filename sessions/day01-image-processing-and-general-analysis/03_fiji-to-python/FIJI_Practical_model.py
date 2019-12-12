#good review of jython for fiji at #https://www.ini.uzh.ch/~acardona/fiji-tutorial/
#Many students noticed that the recorder works much better for this when set to JavaScript.  
#Thanks to them for noticing.

from ij import IJ #load the FIJI modules
from ij.io import FileSaver
from ij.io import OpenDialog
from ij.measure import ResultsTable

IJ.run("Clear Results");  #clear results

od = OpenDialog("Choose a file", None)
filename = od.getFileName()
directory =  od.getDirectory()
path = od.getPath()

print filename   #print filename, directory, path out to log box for sanity check
print directory
print path

imp = IJ.openImage(path)
imp.show()

IJ.run(imp, "8-bit", "");
IJ.run(imp, "Make Binary", "");
IJ.run(imp, "Watershed", "");
IJ.run("Set Measurements...", "area min redirect=None decimal=3"); #set measurements
IJ.run(imp, "Analyze Particles...", "display");
IJ.run(imp, "Close All", "");

#save the results table as a CSV
save_string = directory + 'Results_practical.csv' #generate a string to save file to image directory
IJ.saveAs("Results", save_string);

