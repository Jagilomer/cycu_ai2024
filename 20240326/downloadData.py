import requests
import os

base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240325/"

# Create a directory to store the downloaded files
os.makedirs('downloaded_files', exist_ok=True)

# Loop over each hour
for hour in range(24):
    # Loop over each minute
    for minute in range(60):
        # Create the file URL
        file_url = base_url + f"{hour:02d}/{'TDCS_M05A_20240325_' + str(hour).zfill(2) + str(minute).zfill(2) + '00.csv'}"

        # Send a GET request to the file URL
        response = requests.get(file_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Write the content of the response to a CSV file
            with open(f"20240326/downloaded_files/TDCS_M05A_20240325_{hour:02d}{minute:02d}00.csv", 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download file from {file_url}")
            
            