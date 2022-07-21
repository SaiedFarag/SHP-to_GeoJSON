'''
SHP to GeoJSON converter
created by Saied Farag
07/10/2022
'''

import geopandas as gpd
import fiona
import os

# Define path and name of the input shapefile
inName = input('Enter the name of the input shapefile: ') + '.shp'
in_path = os.path.join('in_SHP', inName)
print(in_path)

# Define the name and path of the output GeoJSON file
outName = input('Enter the name of the new GeoJSON file: ') + '.geojson'
out_path = os.path.join('out_GeoJSON', outName)
print(out_path)

# reading the input shapefile
in_shp = gpd.read_file(in_path)
print(type(in_shp))

# Check crs
oldCRS = in_shp.crs
print(f'old crs is: {oldCRS}')

# set the crs of the shapefile to epsg=4326
in_shp = in_shp.to_crs(epsg=4326)
newCRS = in_shp.crs
print(f'new crs is: {newCRS}')

# export the output GeoJSON
newJSON = in_shp.to_file(out_path, driver = 'GeoJSON')
print(newJSON)
print('Done!!!')