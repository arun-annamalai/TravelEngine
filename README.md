# TravelEngine
We developed this API to assist vacationers with choosing between hotels when there are a multitude of factors to consider. The API will ask users to prioritize different destinations on their trip (restaurants, parks, architecture, museums, etc.) and will then use k-means clustering to find an ideal location to stay within the city. The user will then have the ability to see up to 3 hotels that are in the ideal location, but differ by price or class. The use case will be for vacationers who may be visiting a city for the first time, and want to maximize their time spent there and not deal with the hassle of travel websites and dozens of options. 


# Setup

To install this command line application please run the script below on a unix system. Make sure your system has python3 installed
```
chmod +x bin/install
./bin/install
```

# Usage

To use this algorithm please type the following into your terminal 
```
cd ./travelengine/user_pref/
python3 userfront.py 
```

# Sample Picture
<img src=https://github.com/arun-annamalai/TravelEngine/blob/c2bf6f536d3686cecd5f4d7f6c570a7c9e1c0007/sample.png>

# Future Road Map
Later down the line, we plan to add the functionality to filter hotels by certain brands so that users can benefit from their past rewards. 

# Credits
Google Maps, opentripmap
