# -*- coding: utf-8 -*-
"""Map.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LEQlxuFSDKFLAOLqumunhxAaK4-Ji2m8
"""

import pandas as pd
import numpy as np
import requests
import datetime
import folium
from folium import plugins
import ipywidgets as widgets
from ipywidgets import interactive
from IPython.display import display
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='myapp')
location = geolocator.geocode('San Jose')
print(location.address)
print(location.latitude, location.longitude)

m1 = folium.Map([37.3361905, -121.890583], zoom_start =11, tiles='Stamen Terrain')
m1

from google.colab import drive
drive.mount('/content/drive')

cd '/content/drive/My Drive/'

cities_geo = '/content/drive/My Drive/Asian_Hate_Crime_Rate.csv'

df = pd.read_csv('/content/drive/My Drive/Asian_Hate_Crime_Rate.csv')
df