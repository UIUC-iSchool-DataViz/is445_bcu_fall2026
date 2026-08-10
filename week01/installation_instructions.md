---
title: OPTIONAL - Installation Instructions
layout: assignment
description: Install necessary packages for this class
---

## These instructions are only if you are already comfortable with conda! 

Please note as of Fall 2023, all assessments will be completed on the PrairieLearn system.  These instructions remain in case you want to install packages locally but please note we will **NOT** be supporting this installation process and you will be "on your own" to get this to work on your machine (for example, if you have a space in your username on your computer, conda is going to give you issues that you need to sort out on your own).

Additionally, packages you install locally may provide different interfaces than those on PrairieLearn -- *it is your responsibility to ensure your code works on your PrairieLearn submission.*

## Installation command

The command to install the DataViz environment on your local computer (Mac Terminal/Windows Anaconda Prompt) is:

```bash
conda create -n DataViz python=3.12 seaborn plotly pygraphviz pandas matplotlib bqplot=0.12.30 numpy regex networkx openssl altair=6.0.0 yt geopandas gdal rasterio shapely pyproj rtree fiona pillow palettable h5py contextily webcolors openpyxl ipyleaflet vega_datasets nltk wordcloud pip -c conda-forge ; conda activate DataViz ; pip install streamlit
```

### Other ways to install locally
1. If you are familiar with docker, you can access the docker image for the workspaces at `jnaiman/workspace-is445`. 
1. To install via a conda env yaml file, you have 2 options:
  1. This [environment_pl.yml](env_files/environment_pl.yml) file is packages as installed on PrairieLearn (preferred)
  1. This [environment_local.yml](env_files/environment_local.yml) file is my local installation of packages

<hr />
<hr />

