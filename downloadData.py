import feedparser
import pandas as pd
import matplotlib.pyplot as plt

# List of RSS URLs
rss_urls = [f"https://www.cwa.gov.tw/rss/forecast/36_{str(i).zfill(2)}.xml" for i in range(1, 23)]

# Create an empty DataFrame
df = pd.DataFrame(columns=["Title", "Description"])

# Loop over each RSS URL
for rss_url in rss_urls:
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Loop over each entry in the feed
    for entry in feed.entries:
        # Add the title and description of the entry to the DataFrame
        df = df.append({"Title": entry.title, "Description": entry.description}, ignore_index=True)

# Print the DataFrame
print(df)

# Plot a bar chart of the number of entries per title
df['Title'].value_counts().plot(kind='bar')
plt.show()