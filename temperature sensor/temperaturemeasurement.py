import json
import sys
from iotticket.models import device
from iotticket.models import criteria
from iotticket.models import deviceattribute
from iotticket.models import datanodesvalue
from iotticket.client import Client

data = json.load(open(sys.argv[1]))
username = data["username"]
password = data["password"]
baseurl = data["baseurl"]
c= Client(baseurl,username,password)
if(c!="404 URL NOT FOUND!!!"):
	d = device()
	d.set_name("Raspi Temperature Sensor")
	d.set_manufacturer("Wapice")
	d.set_type("Sensor")
	d.set_description("Temperature sensor")
	d.set_attributes(deviceattribute("Sensor model","DS18B20"))
	resp = c.registerdevice(d)
	data={"username":username,"password":password,"deviceId":resp.get_deviceId(),"baseurl":baseurl}
	with open("write.json","w") as outfile:
		json.dump(data, outfile, sort_keys=True, indent=4)
	print(resp.get_deviceId())

else:
	print(c)