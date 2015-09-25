import sys
import json
import csv
import urllib2

# format note...I know I still need to work on code line length!

if __name__=="__main__":
	#pull url and concatenate with key and bus line
	mta_url = ("http://api.prod.obanyc.com/api/siri/"
				"vehicle-monitoring.json?key=%s"
				"&VehicleMonitoringDetailLevel=calls&LineRef=%s") % (sys.argv[1],sys.argv[2])

	#open url and save in a variable
	get_mta = urllib2.urlopen(mta_url)	

	#load json into python object(variable)
	bus_data = json.load(get_mta)

	#select all buses
	buses = bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

	#open and write to csv file
	with open(sys.argv[3], 'wb') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])

	# information on bus x's closest stop and its status relative to that stop and writes into csv
	# this does not provide info about any of the other stops relative to each bus, just the closest ("Onward Call[0]")
		for bus in buses:
			busLat = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
			busLon = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
			if len(bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']) > 0:
				stopName = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
				stopStatus = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
			else:
				stopName = "N/A"
				stopStatus = "N/A"
			row = [busLat, busLon, stopName, stopStatus]
			writer.writerow(row)