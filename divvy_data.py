import json
import urllib2
import pprint

'''
DIVVY DATA STRUCTURE
executionTime
	- Time of creation
stationBeanList
	- Array of bike stations

Bike Station:
[u'availableDocks',
 u'totalDocks',
 u'city',
 u'altitude',
 u'stAddress2',
 u'longitude',
 u'lastCommunicationTime',
 u'postalCode',
 u'statusValue',
 u'testStation',
 u'stAddress1',
 u'stationName',
 u'landMark',
 u'latitude',
 u'statusKey',
 u'availableBikes',
 u'id',
 u'location']
'''
DIVVY_URL = "http://divvybikes.com/stations/json"
class StationList:
	def __init__(self):
		data = _get_data()
		self.stations = []
		self.time = data['executionTime']
		for station in data['stationBeanList']:
			self.stations.append(Station(station))


	def refresh(self):
		self.__init__()


class Station:
	def __init__(self, station_dict):
		self._station_dict = station_dict
		self.availableDocks = station_dict['availableDocks']
		self.totalDocks = station_dict['totalDocks']
		self.city = station_dict['city']
		self.altitude = station_dict['altitude']
		self.stAddress2 = station_dict['stAddress2']
		self.longitude = station_dict['longitude']
		self.lastCommunicationTime = station_dict['lastCommunicationTime']
		self.postalCode = station_dict['postalCode']
		self.statusValue = station_dict['statusValue']
		self.testStation = station_dict['testStation']
		self.stAddress1 = station_dict['stAddress1']
		self.stationName = station_dict['stationName']
		self.landMark = station_dict['landMark']
		self.latitude = station_dict['latitude']
		self.statusKey = station_dict['statusKey']
		self.availableBikes = station_dict['availableBikes']
		self.id = station_dict['id']
		self.location = station_dict['location']

	def fraction_open(self):
		return float(self.availableDocks) / self.totalDocks


	def __str__(self):
		return str(self._station_dict)

def _get_data():
	json_file = urllib2.urlopen(DIVVY_URL)
	data = json.load(json_file)
	return data










