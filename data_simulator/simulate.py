import json
import notecard
import notecard_pseudo_sensor
from periphery import I2C
import time

productUID = "com..your-name:your_product"

port = I2C("/dev/i2c-1")
card = notecard.OpenI2C(port, 0, 0)

req = {"req": "hub.set"}
req["product"] = productUID
req["mode"] = "continuous"
 
print(json.dumps(req))
 
rsp = card.Transaction(req)
print(rsp)

