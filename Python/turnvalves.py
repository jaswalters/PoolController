import webiopi
import json

GPIO = webiopi.GPIO

@webiopi.macro
def FountainModeOn():
    GPIO.digitalWrite(23, GPIO.HIGH)
    GPIO.digitalWrite(18, GPIO.HIGH)
    pyjson = {"Mode": "FountainMode"}
    return json.dumps(pyjson,indent=4, separators=(", ", ": "))

@webiopi.macro
def FountainModeOff():
    GPIO.digitalWrite(23, GPIO.LOW)
    GPIO.digitalWrite(18, GPIO.LOW)
    pyjson = {"Mode": "FountainModeOff"}
    return json.dumps(pyjson,indent=4, separators=(", ", ": "))

@webiopi.macro
def WaterFallModeOn():
    GPIO.digitalWrite(23, GPIO.HIGH)
    GPIO.digitalWrite(18, GPIO.HIGH)
    pyjson = {"Mode": "WaterFallMode"}
    return json.dumps(pyjson,indent=4, separators=(", ", ": "))

@webiopi.macro
def WaterFallModeOff():
    GPIO.digitalWrite(23, GPIO.LOW)
    GPIO.digitalWrite(18, GPIO.LOW)
    pyjson = {"Mode": "WaterFallModeOff"}
    return json.dumps(pyjson,indent=4, separators=(", ", ": "))

@webiopi.macro
def SpaModeOn():
    GPIO.digitalWrite(23, GPIO.HIGH)
    GPIO.digitalWrite(18, GPIO.HIGH)
    pyjson = {"Mode": "SpaMode"}
    return json.dumps(pyjson,indent=4, separators=(", ", ": "))

@webiopi.macro
def SpaModeOff():
    GPIO.digitalWrite(23, GPIO.LOW)
    GPIO.digitalWrite(18, GPIO.LOW)
    pyjson = {"Mode": "SpaModeOff"}
    return json.dumps(pyjson,indent=4, separators=(", ", ": ")
