# Import necessary modules
from urllib.request import urlopen
import os

# Define the URL and file paths
url = "http://cheer.lib-dyndns.com/.?cheerid"
file_name = "C:\\xampp\\htdocs\\here\\heresay\\here.php"

# Fetch the webpage data
data = urlopen(url).read()

# Check if the file already exists
if os.path.exists(file_name):
    print("File exists")
else:

    with open(file_name, "wb") as f:
        f.write(data)
    print("File created and data written")
