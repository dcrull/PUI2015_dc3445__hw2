import sys
import csv
import json
import urllib2

if __name__=="__main__":
	#pull url and concatenate with key and bus line
	mta_url = ("http://api.prod.obanyc.com/api/siri/"
				"vehicle-monitoring.json?key=%s"
				"&VehicleMonitoringDetailLevel=calls&LineRef=%s") % (sys.argv[1],
																	 sys.argv[2])

	#open url and save in a variable
	get_mta = urllib2.urlopen(mta_url)	

	#load json into python object(variable)
	bus_data = json.load(get_mta)

	#select all buses
	buses = bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	
	#print bus line - as verified by the JSON, not the command line argument
	print "Bus Line : %s" % buses[0]["MonitoredVehicleJourney"]["PublishedLineName"]

	#print number of active buses
	print "Number of Active Buses : %s" % len(buses)

	#print bus x and bus x's lat/long
	count = 0
	for bus in buses:
		print "Bus %s is at latitude %s and longitude %s" % (
				count,
				bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],
				bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
		count+=1
