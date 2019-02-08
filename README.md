# SmartThings Pool Controller

This is my first device handler for SmartThings

I wanted to create a pool controller for swiching modes in our pool and will eventually add the vacuum and other items in later. Hopefully this will either help someone along that is looking to do similiar or give you just what you need.

Right now I do not have any valves I'm running the testing with a bread board and lighting up some LEDs. This is working great and the goolge assistant integration through IFTTT is a nice have.

This project requires stretch OS on Raspberry Pi.
WEBIOPI setup on the RPi.
http://webiopi.trouch.com/

In WEBIOPI I set the startup config file to enable the GPIO's I'm using to output so each time the RPi starts up the GPIO's will be accessible. You can change the GPIO's or use the same in the Python scripts.

The Pool Controller works like this, when you click to change a mode it will turn off the pump before turning any valves as this is safer with my pump configuration. After the pump is off the modes will start changing and you will see the current mode turining off and the new mode turning on.

If you click restart it will make a call to the RPi to reboot and display rebooting under the RPi symbol.

There are also verious monitors to keep track of CPU, disk space usage, memory and CPU temp.

Google Assistant Integration:

To integrate with Google Assistant you will need to create a piston in WebCore and create an IFTTT recipe that calls the piston. The recipe uses Google Assistant and WebHook.

The Google Assistant file on GitHub shows the url that you append to the external piston url in order for IFTTT to make the call to your piston with the proper parameters.

