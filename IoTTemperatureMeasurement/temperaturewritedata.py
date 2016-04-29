import time
import json
import sys
import datetime
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

while 1:
	c = Client(baseurl,username,password)	
	tempfile = open("/sys/bus/w1/devices/28-000006b19b27/w1_slave")
	text = tempfile.read()
	tempfile.close()
	tempdata = text.split("\n")[1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature = temperature/1000
	nv = datanodesvalue()
	nv.set_name("Sensor temperature")
	nv.set_path("tempVal")
	nv.set_dataType("double")
	nv.set_unit("deg")
	nv.set_value(temperature)
	nv.set_timestamp(c.dttots(datetime.datetime.now()))
	c.writedata(deviceId, nv)
	print("v: " + str(nv.get_value()) +"\nts: " + str(nv.get_timstamp()) + "\n")
	time.sleep(2)