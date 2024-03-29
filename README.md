[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11547430&assignment_repo_type=AssignmentRepo)
# An end to end Data Science Project
- Name: `Muhammad Usman`

**Research Goal:** Determinants of Yellow Taxi Demand in New York City

**Timeline:** The timeline for the research area is 2022 - 2023 (Post COVID-19)

**Project Report** You can find the final project report in diretory `report`

## Please run all the files in order!

### Move to the `scripts` directory and run the following file to download data
- `download.py`: This downloads the raw **Yellow taxi** data into the `data/landing` directory. Raw **weather** data is downloaded
into `data/weather` directory.

**NOTE** that `.py` files are considered running from root directory for this project. So, files paths to store data are relative to the root directory. **Modify** paths as per your specification if needed.


### After successfully downloading the raw data move to the `notebooks` directory and run the following files in `order`:
1. `preprocess.ipynb`: This notebook details all preprocessing steps and outputs it to the `data/raw` and `data/curated` directory
for **Yellow taxi** data. For **weather** data it outputs to `data/weather_curated` directory after preprocessing. **This notebook is also used for outlier detection and removal**.

2. `analysis.ipynb`: This notebook is used to conduct analysis on the curated data and outputs any plots produced to the `plots` directory.

3. `model.ipynb`: This notebook is used to conduct modelling on the curated data and outputs any plots produced to the `plots` directory.

**NOTE** that `.ipynb` files are considered running from their own directory. So, files paths to store data/plots are relative to the notebook directory. **Modify** paths as per your specification if needed.


# NOTE:
### NYC zones data is taken from University of Melbourne MAST30034 Tutorial 2 and can be found in data/taxi_zones
### Weather data URL in scripts/download.py expires by 27th August, so, for the feasibility landing weather data can be found in data/weather in this repo. However, you can request another link from this website https://www.ncei.noaa.gov/cdo-web/search
