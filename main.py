# import .csv files into Blender
# (this script has only been tested for Mac)

# running this script in Blender will generate a mesh with vertices
# positioned at each (x, y, z) corrdinate in a specified .csv file

import bpy
import csv
import pathlib


# ———————— import the .csv data ————————
file_loc = pathlib.Path(__file__).parent.resolve() # location of .blend file to receive imported data
folder = pathlib.Path(file_loc).parent.resolve() # location of the folder containing our .blend file

data = pathlib.Path(folder).joinpath('coordinates.csv') # the .csv file to import (within the same folder as .blend file)

coll = bpy.data.collections['Collection']

# clean scene
#for ob in coll.objects:
#    bpy.data.remove(ob) # only run this if you want to delete everything in the collection


# ——————— read and store .csv coordinate data ————————
vertices = []
edges = []
faces = []

with open(data, 'r') as csvfile:
    datareader = csv.reader(csvfile) # this is our reader vairable
    next(datareader) # skip the first line (as it's usually a row of headers)
    i = 0
    for row in datareader: # for every row in the spreadsheet
        vertices.append((i, float(row[3]), 0)) # create a (i, row[column], 0) for a (x, y, z) vertex
        i += 1


# ——————— create a mesh and an object from the coordinate data ————————
new_mesh = bpy.data.meshes.new('data')
new_mesh.from_pydata(vertices, edges, faces)
new_mesh.update()

# create an object to join with the mesh data
new_object = bpy.data.objects.new('data_graph', new_mesh) # the name 'data_graph' can be changed
coll.objects.link(new_object) # link our new object to the collection
