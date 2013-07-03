divvy_bikes_python
==================

divvy_bikes_python is a Python wrapper for Divvy, Chicago's Bike Sharing system. 

Example Usage
---------------------
```python
import divvy_data as dd

# Get a list of all bike station locations
sl = dd.StationList() # Represents a list of bike docking stations
for station in sl.stations:
    print station.stationName
```

