# Tracking course
## Getting users on Python
- PDF document with how to install Conda on Windows/Mac/Linux
- Installation of libraries/packages
- environment.yaml configuration file

## Presentation
- Tracking algorithms
  - Centroid tracking using Hungarian algorithm
    - Limiting linking distance
    - Improving tracking using alternative/additional metrics
  - Splitting/merging
  - Track refinement using Kalman filter
  - Demonstrate existing Python libraries/packages for tracking?
- Track analysis
  - RMSD
  - Directionality
  - Radial statistics (mean, etc.)
- Track visualisation
  - Create projected image (easier to view than Z-stack)
  - Display lines (colour-coded) for each track (limited history)
  - Display tracks as overlay on image.
- Data visualisation
 - Display numeric plot of (for example), RMSD

## Practical
- Provided materials
  - XYZT coordinates in text file
    - Coordinates from online tracking challenge (e.g. http://celltrackingchallenge.net/3d-datasets/)
    - Possibly include other metrics (e.g. size, intensity)
  - Image (already projected?) to display tracks on
  - Code to import coordinates (limited time, so don't want to waste it)
  - Code to test output coordinates against "correct" results.
    - This won't be provided until towards the end.
- Aim
  - Track objects from provided coordinates
  - Get closest to actual track results (hence using coordinates from an online challenge)
  - Export to specific format (Z,Y,Z,T,ID)
  - Get a score for accuracy of track annotations
