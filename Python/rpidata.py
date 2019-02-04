import webiopi
import json
import psutil
import os

@webiopi.macro
def getRPiData():
    #Get cpu usage
    cpuUsage = psutil.cpu_percent(interval=1)
    #Get memory usage
    memUsage = psutil.virtual_memory().percent
    #Get disk usage
    diskUsage = psutil.disk_usage('/').percent
    #Get cpu temp
    temps = psutil.sensors_temperatures()
    for name, entries in temps.items():
        for entry in entries:
        #print(entry.current)
            ftemp = (entry.current * 9/5) + 32
    ftemprnd = str(round(ftemp, 1))
    #pyjson = { "cpu_usage": cpuUsage }
    pyjson = { "cpu_usage": cpuUsage, "cpu_temp": ftemprnd, "disk_usage": diskUsage, "mem_usage": memUsage }
    return json.dumps(pyjson,indent=4, separators=(", ", ": "))

@webiopi.macro
def rebootRPi():
    os.system("sudo reboot")
    pyjson = { "reboot": true }
    return json.dumps(pyjson,indent=4, separators=(", ", ": "))