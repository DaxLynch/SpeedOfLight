from geopy.distance import distance
import requests
from ip2geotools.databases.noncommercial import DbIpCity
import re
import json
import pandas as pd

# Make a regular expression
# for validating an Ip-address
regex = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

urls = ["www.ecobank.com", "esunbank.com", "cam.ac.uk", "sun.ac.za", "cern.ch", "sydney.edu.au", "ufl.edu","berkeley.edu"]
distances = []
cities = []
times = []
timesSTD = []
hops = []

#The .ping and .trc files were created with the script.sh
#The trace files I removed the first 2 lines and any lines after the final server, i.e. those that say no replyexit
#NOTE
#for some of the cities the DB returns, they are incorrect. For Berkeley it was returning a distance of 26,000km because it was reporting some of the intermediate cities being in the UK. TO get around this I had to do Berkeley by hand. This could be fixed by using a better IP database, which the module does allow for.

for url in urls:
    ipList = []
    f = open(url + ".trc", "r")
    trcLine = f.readline()
    maxHops = 0
    while(trcLine): #This goes through each trc file and gets an IP for each hop
        maxHops = int(trcLine.split(':')[0].strip())
        IP = re.search(regex, trcLine)

        if (IP != None):
            ipList.append(IP.group(0))

        trcLine = f.readline()

    res = DbIpCity.get(ipList[0], api_key="free")
    oldTup = (res.latitude, res.longitude); #This is the location of the first server
    totalDistance = 0
    res = 0;
    cityList = []
    print(url)
    for ip in ipList: #This gets the distance for each hop, and if the hop is into a new city, it adds it to the cities list
        res = DbIpCity.get(ip, api_key="free")
        tup = (res.latitude, res.longitude);
        if (res.city not in cityList) and (res.city != None):
            print(res.city)
            cityList.append(res.city)
            totalDistance += distance(tup, oldTup).km
            print("__________________")
        oldTup = tup

    ping = url
    ping = open(ping + ".ping", "r")
    ping = ping.readlines()[-1] #This reads the final line of the ping file, and the code below gives the average and std. dev
    pingAve = float(ping.split("/")[4])
    pingStd = float(ping.split("/")[6].split()[0])
    
    times.append(pingAve)
    timesSTD.append(pingStd)
    hops.append(maxHops)
    distances.append(totalDistance)
    cities.append(len(cityList))

    print("The final distance to " + res.city + " is: " + str(totalDistance))
    print("The ping is " + str(pingAve) + " and the std. deviation is " + str(pingStd) + ", with maxhops: " + str(maxHops))
    timeForLight = 2*totalDistance*1000/(float(pingAve)/1000)
    print("The estimate for the speed of light is " + str(timeForLight))

#This puts everything into a pandas dataframe.
data = pd.DataFrame((urls,distances,cities,hops,times, timesSTD))
data = data.transpose()
data = data.set_index(0)
data.columns=["Distances","Cities","Hops","Times","Times Std. Dev"]
data["Distances"] *= 1000
data["Times Std. Dev"] /= 1000
data["Times"] /= 1000
f = open("data.json", 'w') #Stores the data object into a file
data.to_json(path_or_buf=f)
f.close()
