# ------------------------------------------------------------------------------
# SETUP VIRTUAL ENVIRONMENT
# ------------------------------------------------------------------------------
# Tutorial on how to create a virtual environment and activate it. https://www.youtube.com/watch?v=1F-oWf5VYSk
# In terminal...
# py -m venv open_buildings_env
# open_buildings_env\Scripts\activate 
# ------------------------------------------------------------------------------
# SETUP PYTHON PACKAGES
# ------------------------------------------------------------------------------
# For gdal and s2geometry, the package requires a C++ compiler and swig. If you are using Windows, you can install Visual Studio Build Tools.
# 1--download VS Build Tools from https://visualstudio.microsoft.com/visual-cpp-build-tools/ check "Desktop development with C++" and install it.
# 2--install Cmake for windows --> winget install Kitware.Cmake
# 3--install swig for windows --> winget insall swig
# 4--upgrade pip installer --> pip install --upgrade pip setuptools wheel cmake_build_extension
# 5--install gdal --> pip install --index https://gisidx.github.io/gwi gdal (https://www.reddit.com/r/gis/comments/1oiruhf/a_new_easy_way_on_windows_to_pip_install_gdal_and/) (https://pypi.org/project/GDAL/)
### 6--install s2geometry (??? still unsure)

import functools
import glob
import gzip
import csv
import multiprocessing
import os
import shutil
import tempfile
from typing import List, Optional, Tuple

import geopandas as gpd
# from google.colab import files
from IPython import display
from mpl_toolkits.axes_grid1 import make_axes_locatable
from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import s2sphere as s2 #use this instead of s2geometry for now as it doesn't need the C++ compiler and swig to install.
# import s2geometry as s2
import shapely
import tensorflow as tf
import tqdm.notebook

# ------------------------------------------------------------------------------
# OPEN FILES
# ------------------------------------------------------------------------------
# .csv.gzip files were downloaded from the CoLab Workbook Az-application-openbuildings https://colab.research.google.com/drive/1OysZ6m8fUx7PKf3gOLe2a_vAcCxIHbdu?usp=sharing
# The downloaded data files were manually moved from Download folder into Az-data folder.

def visual_raw_by_country (country, viz_sample):
  df = pd.read_csv('./spatial-coastal-ses/Az-data/open_buildings_v3_points_ne_110m_'+country+'.csv.gz', encoding='utf-8')

  buildings_sample = (df.sample(viz_sample)
                      if len(df) > viz_sample else df)
  plt.plot(buildings_sample.longitude, buildings_sample.latitude, 'k.',
          alpha=0.25, markersize=0.5)
  plt.gcf().set_size_inches(10, 10)
  plt.xlabel('Longitude')
  plt.ylabel('Latitude')
  plt.axis('equal')
  plt.savefig('./spatial-coastal-ses/Az-graph_output/'+country+'.png', transparent=True, dpi=150)
  plt.close()

  return df

  # df_combined = pd.concat([region, df], ignore_index=True)
  # return df_combined

sample_size = 20000 #help making it quicker to visualize the data.

KHM = visual_raw_by_country(country='KHM', viz_sample=sample_size)
IDN = visual_raw_by_country(country='IDN', viz_sample=100000)
MYS = visual_raw_by_country(country='MYS', viz_sample=sample_size)
PHL = visual_raw_by_country(country='PHL', viz_sample=sample_size)
THA = visual_raw_by_country(country='THA', viz_sample=sample_size)
VNM = visual_raw_by_country(country='VNM', viz_sample=50000)

SEA_region = pd.concat([KHM, IDN, MYS, PHL, THA, VNM], ignore_index=True)




