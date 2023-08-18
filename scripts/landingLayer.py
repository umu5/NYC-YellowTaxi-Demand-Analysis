# Please run this file using University's network. Accessing TLC data using
# local network will make the process very slow or may result in connection
# error.

# run this file from root durectory of the project such as using command
# `python scripts/landingLayer.py`

import os
from urllib.request import urlretrieve

print(os.getcwd())

# directory to store all incoming TLC data
if not os.path.exists('data/tlc/'):
    os.mkdir('data/tlc/')

# directory to store all incoming weather data
if not os.path.exists('data/weather/'):
    os.mkdir('data/weather/')


# Now downloading TLC (yellow taxi) data
URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"
# data output directory is `data/tlc_data/`
tlc_output_dir = 'data/tlc/'

def year_data(year, months):
    """Following function has been adapted from pre req Notebook provided in 
    MAST30034. This function downloads the data from the TLC website for the 
    given year and months and saves it to the tlc_output_dir directory. `Year` 
    is String and months is a `range`
    """
    i = 0
    for month in months:
        month = str(month).zfill(2) 
        # generate url
        url = f'{URL_TEMPLATE}{year}-{month}.parquet'
        # generate output location and filename
        output_dir = f"{tlc_output_dir}/{year}-{month}.parquet"
        # download
        urlretrieve(url, output_dir)
        i += 1
        print(f'yellow taxi data for {year}-{month} successfully downloaded')

    print(f'year - {year} data finished total months data successfully '
          f'downloaded from this year: {i}\n')

# download Yellow taxi records from 2022 January - 2023 May  (post Covid data)
year_data('2022', range(1,13))
year_data('2023', range(1,6))