

import time
import json
import sys
import datetime
sys.path.append('/home/pi/IoTTicket-PythonLibrary')

from iotticket.models import device
from iotticket.models import criteria
from iotticket.models import deviceattribute
from iotticket.models import vts
from iotticket.models import datanodesvalue
from iotticket.client import Client

data = json.load(open(sys.argv[1]))
username = data["username"]
password = data["password"]
deviceId = data["deviceId"]
baseurl = data["baseurl"]

#create client object
c = Client(baseurl,username,password)	
tempfile = open("/home/pi/IoT-ticket/" + sys.argv[2] + ".data")
text = tempfile.read()
tempfile.close()	
temperature = float(text)

nv = datanodesvalue()
nv.set_name(sys.argv[2])
nv.set_path("TelldusNetwork")
nv.set_dataType("double")

nv.set_unit("deg")

	
#set the value of the node with the temperature value
nv.set_value(temperature)
#set the timestamp as now
nv.set_timestamp(c.dttots(datetime.datetime.now()))
#call writedata function
c.writedata(deviceId, nv)
print("v: " + str(nv.get_value()) +"\nts: " + str(nv.get_timstamp()) + "\n")
#the program will run every 2 seconds
	
