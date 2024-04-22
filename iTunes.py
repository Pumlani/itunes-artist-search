import json  # Importing the JSON module for handling JSON data
import requests  # Importing the Requests module for making HTTP requests
import sys  # Importing the sys module for system-specific parameters and functions

if len(sys.argv) != 2:  # Checking if exactly one command-line argument is provided
    sys.exit()  # Exiting the script if the condition is not met

# Making an HTTP GET request to the iTunes API with the search term provided as a command-line argument
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

# Parsing the JSON response into a Python dictionary
object_json = response.json() 

# Iterating over each result in the JSON response and printing the track name
for result in object_json["results"]:
    print(result["trackName"])
