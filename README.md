This script was developed while resolving assymetric features in cryo-EM reconstruction workflows of icoshedral viruses. Viruses often feature assymetric structures on some vertices. We found that a simple way of identifying and pooling particle images of these structures is to recenter the box on vertices, followed by focused 3D classification. We found that this workflow often works best if shifted coordinates are set outward from the vertex surface. By executing this script, you are provided with a spectrum of markers that eminate outward from the vertex surface; coordinates for these markers are then printed to the log in xyz voxel format for use in reconstruction programs. From our experience, a user may need to sample several of these coordinates with varying distances from the vertex surface for this method to work well. We also found that varying box size and using focus masks improved results considerably.


Intructions for use are written in the .py scripts module docstring at the top of the file. The script requires manual modification of several paramters (pixel size, box size, edge length).

Currently, the script only works for capsids resolved with I2 symmetry imposed (working on expanding this). 

This script was primarily used in conjuncture with cryoSPARC, for 3D box recentering in the volume alignment tools utility.
