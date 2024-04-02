import geopandas as gpd
import pandas as pd
import requests
import feedparser
import matplotlib.pyplot as plt

# Fetch weather data
county_list = []
for num in range(1, 23):
    url = 'https://www.cwa.gov.tw/rss/forecast/36_' + str(num).zfill(2) + '.xml'
    response = requests.get(url)
    feed = feedparser.parse(response.content)

    tempdict = {}
    for entry in feed.entries:
        if '溫度' in entry.title:
            tempdict['county'] = entry.title[:3]
            tempdict['min'] = entry.title.split(' ')[-7]
            tempdict['max'] = entry.title.split(' ')[-5]
            county_list.append(tempdict)

df_weather = pd.DataFrame(county_list)

# Read shape file
df_taiwan = gpd.read_file('20240402/county/COUNTY_MOI_1090820.shp')

# Set original CRS and re-project
df_taiwan.crs = "EPSG:4326"
df_taiwan = df_taiwan.to_crs("EPSG:3857")

# Merge DataFrames
geo_taiwan = pd.merge(df_taiwan, df_weather, left_on='COUNTYNAME', right_on='county')

# Plot data
geo_taiwan.plot()
#plt.xlim(118,122)
#plt.ylim(21.5,25.5)

#output countyname at centroid of each polygon
for x, y, label in zip(geo_taiwan.geometry.centroid.x, geo_taiwan.geometry.centroid.y, geo_taiwan['min']):
    plt.text(x, y, label, fontsize=8, ha='center')

for x, y, label in zip(geo_taiwan.geometry.centroid.x, geo_taiwan.geometry.centroid.y, geo_taiwan['max']):
    plt.text(x+ 0.2 , y, label, fontsize=8, ha='center')

# Add title before showing the plot
plt.title('11272014 Chih-Chun Yang')
# ... your code ...

# Save the plot before showing it
plt.savefig('plot.png')

plt.show()
