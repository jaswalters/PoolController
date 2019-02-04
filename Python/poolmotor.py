import webiopi
import json

GPIO = webiopi.GPIO

@webiopi.macro
def PoolPumpOn():
    GPIO.digitalWrite(24, GPIO.HIGH)
    pyjson = {"PoolPump": "On"}
    return json.dumps(pyjson,indent=4, separators=(", ", ": "))

@webiopi.macro
def PoolPumpOff():
    GPIO.digitalWrite(24, GPIO.LOW)
    pyjson = {"PoolPump": "Off"}
    return json.dumps(pyjson,indent=4, separators=(", ", ": "))