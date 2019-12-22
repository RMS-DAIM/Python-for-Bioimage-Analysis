# IAFIG-RMS-bioimage-training
Image Analysis Focused Interest Group of the Royal Microscopy Society Bioimage Analysis Course.

## Aim:
The aim of this week-long course is to develop motivated students/staff toward becoming independent BioImage Analysts in a facility or research role. Students will be taught theory and algorithms relating to bioimage analysis using Python as a coding language.

## Target Audience:
Cell Biologists, Biophysicists, BioImage Analysts with some experience of basic microscopy image analysis. In addition, this course may be of interest to physical scientists looking to develop their knowledge of Python coding in the context of image analysis. This course is appropriate for researchers who are relatively proficient with computers but maybe not had the time or resources available to become programmers. Some prior experience of scripting or modifying scripts would be useful. We ask that all attendees complete a basic Python coding course before the course begins. Details of this will be sent to attendees which apply.

## Learning Outcomes: 
This course will give candidates knowledge of image analysis theory and algorithms:
* It will consolidate and extend their Python coding skills to cover topics relevant to bioimage analysis (see content below). 
* It will give them practise coding algorithms. 
* It will develop their confidence as independent BioImage Analysts, able to understand new algorithms and implement them.
* Candidates will experience developing pipelines which start with raw data and result in publication quality figures and will be able to apply this process in the future.

## Content:
Lectures will focus on Image Analysis theory and application. Topics to be covered include: Image Analysis and image processing, Python and Jupyter notebooks, Visualisation, Fiji to Python, Segmentation, Omero and Python, Image Registration, Colocalisation, Time-series analysis, Tracking, Machine Learning, Applied Machine Learning. The bulk of the practical work will focus on Python and how to code algorithms and handle data using Python. Fiji will be used as a tool to facilitate image analysis. Omero will be described and used for some interactive coding challenges. Research spotlight talks will demonstrate research of instructors/scientists using taught techniques in the wild.

## Prequisites
- Basic awareness of Fiji/ImageJ. You should be able to open images and do basic analysis, basic macro writing is advantageous.
- Python introductory course: https://github.com/ChasNelson1990/python-zero-to-hero-beginners-course
  - If you've not done much Python in the past, you should work your way through the pre-requisite course (approx. 12-15 hr); however, those comfortable in Python may choose to skips components they are confident about.

## Organisers
Dominic Waithe and Gabriella Rustici.
### Co-organisers
Chas Nelson and Stephen Cross.
### Lecturers
Aurelien Barbotin (AB)  
Chas Nelson (CN)  
Dominic Waithe (DW)  
Ola (Alexandra) Tarkowska (OT)  
Mikolaj Kundegorski (MK)  
Stephen Cross (SC)  
Todd Fallesen (TD)  

## Timetable
#### Monday (Image Processing and General Analysis):
- 9:30-10:00: Introduction to course and structure. (DW)
- 10:00-11:50: Images in Python (CN)
- 12:00-13:00: Lunch
- 13:00-14:30: Interactive demonstration: image processing in Python. (CN)
- 15:00-17:00: Interactive demonstration: Fiji to Python. Visualisation (TF). 
#### Tuesday (Segmentation and colocalization):
- 9:30-10:00: Research spotlight talk. (SC, 25+5 min, “Just keep swimming: Characterising motion of zebrafish")
- 10:00-10:50: Segmentation (DW)
- 11:00-12:30: Practical (DW)
- 12:30-13:30: Lunch
- 13:30-14:30: Colocalisation and Registration (DW)
- 15:00-17:00: Practical (DW)
#### Wednesday (ImageJ Interaction and OMERO interaction):
- 9:30-10:00: Research spotlight talk. (Virginie Uhlmann, 25+5 min, “Quantifying morphology from bioimages with parametric model")
- 10:00-10:50: Using ImageJ within Python (CN)
- 11:00-12:30: Practical (CN)
- 12:30-13:30: Lunch
- 13:30-15:00: OMERO and Python interfacing (DW)
- 15:00-17:00: Free time
#### Thursday (Tracking and Time Series):
- 9:30-10:00: Research spotlight talk (AB, 25+5 min, “Python in applied research"). 
- 10:00-10:50: Data Fitting and Time Series Analysis (DW).
- 11:00-12:30: Practical (time-series analysis exercises)(DW).
- 12:30-13:30: Lunch
- 13:30-14:30: Tracking (e.g. cell tracking). (SC)
- 15:00-17:00: Practical on tracking (SC)
#### Friday (Machine Learning for Bioimage Analysis):
- 9:30-10:00: Research spotlight talk. (DW, 25+5 min, “Automating microscopy acquisition with deep learning”)
- 10:00-10:50: Introduction to Machine Learning for Bioimage analysis. (MK)
- 11:00-12:30: Practical.(MK)
- 12:30-13:30: Lunch
- 13:30-14:30: BioImage analysis Applied machine learning. (MK)
- 15:00-17:00: Practical (MK)

## How to use this repository

This repository contains the materials used during the course. We will create a new 'release' each time we run this course.

The following instructions assume you have installed the Python 3.7 version of Anaconda for you computer; see https://www.anaconda.com/distribution/#download-section for download links and instructions. They are also aimed a Jupyter Lab interface (which uses ipynb notebooks) and not the older Jupyter Notebook interface (which also uses ipynb notebooks).

To get the materials for your version of the course please download the zip for that release by going to clicking the 'X releases' link above. To get the latest materials please download the zip (using the green button above).

1. Unzip the downloaded file.
2. Open a terminal and navigate to the unzipped folder, e.g. `cd ./Python-for-Bioimage-Analysis/`.
3. Run `conda env create -f environment.yml`. This installs all the prerequisite packages for the course in a virtual environment called 'bioimage'.
4. Run `conda activate bioimage`. This moves you into the virtual environment.
5. Run `python3 -m ipykernel install --user --name=bioimage`. This makes this virtual environment available as a kernel in Jupyter lab.
6. Run `conda deactivate` to leave the virtual environment.
7. Start Jupyter Lab, either through Anaconda Navigator or by running `jupyter lab` in a terminal.

You will need to change the kernel for each notebook from the default 'Python 3' notebook to the 'bioimage' notebook. You can do this by clicking where it says 'Python 3' in the top right or bottom left of a Jupyter Lab window.

### Issues with %matplotlib widget

Using `%matplotlib widget` provides interactive elements for plots inside notebooks. However, it is still a young system and sometimes things don't work straight away. The following two issues may occur:

1. Instead of plots you see 'Canvas(...' or similar messages. In this case the jupyter-matplotlib (or `ipympl`) module has not properly installed/been enabled within Jupyter Lab. Completely shutdown Jupyter Lab and follow these instructions:
  * `conda install ipympl nodejs`
  * `jupyter labextension install @jupyter-widgets/jupyterlab-manager`
  * `jupyter labextension install jupyter-matplotlib`
  * `jupyter lab build`
  * Restart Jupyter Lab.
2. Instead of plots you see 'Loading widget...'. You probably just need to completely shut down Jupyter Lab and restart it.
