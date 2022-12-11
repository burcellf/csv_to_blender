# csv_to_blender
a Python script for importing coordinate data from a .csv file to a mesh in Blender

running this code in Blender will:
  1) delete everything in the current .blend file to create a fresh scene (optional)
  2) accept a .csv file as an argument and
      2.1) skip the first line (headers)
      2.2) copy the cell data from the 4th column of every row
      2.3) create a vertex of (row#, celldata, 0)
