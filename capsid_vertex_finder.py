
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ICOSAHEDRON VERTEX COORDINATE VISUALIZATION

This script was made for the visualisation and identification of I2 
icosahedral vertex coordinates. ONLY I2 symmetry is currently 
functional. This script is designed for use in chimeraX 
(latest version recommended). 

Vertex coordinates will be constructed as differently coloured marker sets in 
chimeraX. The log will then print the voxel coordinates of each marker indexed 
by colour for downstream box recentering workflows.

The user must manually update values box size and pixel size. Reducing the 
value edge_start variable will shift the spectrum of vertex coordinates toward the 
capsid centre. Increasing this value will move the spectrum away from the 
capsid center.

The user can thus modify edge_start to find a spectrum of coordinates that 
extend from the capsid surface at varying distances. Undefined name errors 
below are not a problem. The script is executed by opening in chimeraX 
(dragging into the chimeraX window is simplest).   


Created on Sat Jul  1 23:06:12 2023

@author: JimHBean
"""


from chimerax.core.commands import run 


#creates a class that stores information relating to each vertex Point.
class Point:
    def __init__(self, x, y, z, name):
        self.x = x
        self.y = y
        self.z = z
        self.name=name


# User provided reconstruction box size (in voxels).

box = 756

# User provided reconstruction pixel size (in angstroms).

pixel = 1.387

# CHANGE edge_start value to shift spectrum toward the origin (lower numbers) 
# and away from the origin (higher numbers).

edge_start = 560

# Creates a spectrum of varying EDGE lengths; each edge length is used to 
# generate a new set of points at a given radius. 

EDGES = []
for i in range(1,11):
    EDGES.append((edge_start - 150) + i*30 )

# Calculated box center (this is different to the map origin) represented 
# as a point class object.

ORIGIN = Point((box/2) * pixel,(box/2) * pixel,(box/2) * pixel, "ORIGIN")

# Colour spectrum, interpretable by chimeraX.

COLOURS = {1: "red",
    2: "orange",
    3: "yellow",
    4: "lime",
    5: "green",
    6: "teal",
    7: "cyan",
    8: "royal blue",
    9: "blue",
    10: "indigo"}


def main():
    
    # The loop below iterates the action of generating a set of 12 vertex 
    # points for each EDGE value in the EDGES list. 
   
    for IND, EDGE in enumerate(EDGES):
        INDEX = IND+1
        
        # Calculated center of rectangles used to identify vertices.
        
        REC_CENTER = (EDGE*1.618) / 2
        
        # The matrix below generates vertex coordinates for the current EDGE 
        # length.  
        
        VERTICES = [
            
            Point(ORIGIN.x - (EDGE/2), ORIGIN.y, ORIGIN.z + REC_CENTER, "v1"),
            
            Point(ORIGIN.x + (EDGE/2), ORIGIN.y, ORIGIN.z + REC_CENTER, "v2"),
            
            Point(ORIGIN.x - (EDGE/2), ORIGIN.y, ORIGIN.z - REC_CENTER, "v3"),
            
            Point(ORIGIN.x + (EDGE/2), ORIGIN.y, ORIGIN.z - REC_CENTER, "v4"),
            
            Point(ORIGIN.x, ORIGIN.y + REC_CENTER, ORIGIN.z - (EDGE/2), "v5"),
            
            Point(ORIGIN.x, ORIGIN.y + REC_CENTER, ORIGIN.z + (EDGE/2), "v6"),
            
            Point(ORIGIN.x, ORIGIN.y - REC_CENTER, ORIGIN.z - (EDGE/2),"v7"),
            
            Point(ORIGIN.x, ORIGIN.y - REC_CENTER, ORIGIN.z + (EDGE/2), "v8"),
            
            Point(ORIGIN.x + REC_CENTER, ORIGIN.y -(EDGE/2), ORIGIN.z, "v9"),
            
            Point(ORIGIN.x + REC_CENTER, ORIGIN.y +(EDGE/2), ORIGIN.z,"v10"),
            
            Point(ORIGIN.x - REC_CENTER, ORIGIN.y -(EDGE/2), ORIGIN.z, "v11"),
            
            Point(ORIGIN.x - REC_CENTER, ORIGIN.y +(EDGE/2), ORIGIN.z, "v12")
            ]
    
    
        # The loop below plots markers in chimeraX for each set of VERTICES.  
        
        for k, i in enumerate(VERTICES):
            run(session, f"marker #10{INDEX} position {i.x},{i.y},{i.z};")
        
        # Prints to log which coloured marker set the following coordinates 
        # correspond to.
        
        run(session, 
            f"marker change #10{INDEX}  radius 20 color {COLOURS[INDEX]}")
        
        print(f"############### {COLOURS[INDEX]} Points ################# "
              f"\nconverted coordinates: ")

        
        # The loop below converts marker coordinates to integer voxel 
        # coordinates and prints them to the  chimeraX log. Marker Id's 
        # correspond to the printed vertex numbers e.g. mark 5 M = vertex 5.
        
        for k, i in enumerate(VERTICES):
            print(f"vertex {k+1}: {round(i.x/pixel)},{round(i.y/pixel)},"
                  f"{round(i.z/pixel)}")


main()
