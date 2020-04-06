from ij import IJ, ImagePlus #load the FIJI modules
from ij.io import FileSaver
from ij.io import OpenDialog
import os
#from ij.measure import ResultsTable
from fiji.threshold import Auto_Threshold


IJ.run("Clear Results"); 

od = OpenDialog("Choose a file", None)
filename = od.getFileName()
directory =  od.getDirectory()
path = od.getPath()

print filename
print directory
print path

imp = IJ.openImage(path)
imp.show()

IJ.run(imp, "8-bit", "");
imp = IJ.getImage()


hist = imp.getProcessor().getHistogram()
lowTH = Auto_Threshold.Otsu(hist)
print lowTH
imp.getProcessor().threshold(lowTH)
#pulled from http://wiki.cmci.info/documents/120206pyip_cooking/python_imagej_cookbook#pluginauto_threshold

#imp2 = IJ.getImage()
imp.show()

IJ.run("Watershed");

IJ.run("Set Measurements...", "area min redirect=None decimal=3");
IJ.run("Analyze Particles...", "display");
IJ.run(imp, "Properties...", "channels=1 slices=1 frames=1 unit=inch pixel_width=1 pixel_height=1 voxel_depth=1.0000000 global");

print('The width of the image is' , imp.getWidth(), 'pixels')
save_string = directory + 'Results_covid.csv'
IJ.saveAs("Results", save_string);