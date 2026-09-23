# Follow tutorials for GeoPandas: https://www.geopythontutorials.com/introduction.html
# -------------------------------------------------
# 1-Bulk geocoding addresses: https://www.geopythontutorials.com/notebooks/geopandas_bulk_geocoding.html
# -------------------------------------------------
# Data source: NYC Open Data (Hurricane Evacuation Centers): https://data.cityofnewyork.us/Public-Safety/Hurricane-Evacuation-Centers-Map-/ayer-cga7
# What does this line do?
!
%%capture
if 'google.colab' in str(get_ipython()):
    !pip install leafmap mapclassify

import os
import re
import pandas as pd
import geopandas as gpd
import leafmap.foliumap as leafmap
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from zipfile import ZipFile

data_folder = './spatial-coastal-ses/A1-1-data'
output_folder = './spatial-coastal-ses/A1-1-output'

if not os.path.exists(data_folder):
    os.makedirs(data_folder)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def download(url):
    filename = os.path.join(data_folder, os.path.basename(url))
    if not os.path.exists(filename):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filename)
        print('Downloaded' + local)

data_url = 'https://github.com/spatialthoughts/geopython-tutorials/releases/download/data/'
download(data_url + 'hurricane_evacuation_centers.xlsx')

# -------------------------------------------------
# 2-Performing spatial queries: https://www.geopythontutorials.com/notebooks/geopandas_spatial_query.html

# -------------------------------------------------
# 3-Extract a shapefile subset: https://www.geopythontutorials.com/notebooks/geopandas_extract_from_excel.html

# -------------------------------------------------
# 4-Performing fuzzy table joins: https://www.geopythontutorials.com/notebooks/geopandas_fuzzy_table_join.html

# -------------------------------------------------
# 5-Creating a flood inventory map: https://www.geopythontutorials.com/notebooks/geopandas_flood_frequency.html

