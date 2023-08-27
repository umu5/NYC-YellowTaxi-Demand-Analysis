# Please run this file using University's network. Accessing TLC data using
# local network will make the process very slow or may result in connection
# error.

# run this file from root directory of the project such as using command
# `python scripts/download.py`

import os
from urllib.request import urlretrieve
import pandas as pd
from pandas import read_csv

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

print('\nDone with downloading yellow taxi data. Now begin downloading weather' 
      'data\n')


# use this link and download weather data for 2022-01-01 to 2023-05-31
# this is daily summary
# Note that this is link is valid till 27th Aug.
# well my dear tutor due to this reason I have uploaded this data to github
# just wanted to make sure I used an automated process to download this data :))

"""

URL_TEMPLATE2 = "https://www.ncei.noaa.gov/orders/cdo/3427399.csv"
# download weather data csv and save it to data/weather/ and also convert it to
# parquet file
urlretrieve(URL_TEMPLATE2, "data/weather/weather_data.csv")
df = pd.read_csv('data/weather/weather_data.csv')
df.to_parquet('data/weather/weather_data.parquet')
print('weather data successfully downloaded and converted to parquet file')

# now delete that csv file
os.remove('data/weather/weather_data.csv')

"""