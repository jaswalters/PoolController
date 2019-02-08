# SmartThings Pool Controller

This is my first device handler for SmartThings

I wanted to create a pool controller for swiching modes in our pool and will eventually add the vacuum and other items in later. Hopefully this will either help someone along that is looking to do similiar or give you just what you need.

Right now I do not have any valves I'm running the testing of a bread board and lighting up some LEDs. This is working great and the goolge assistant integration through IFTTT is a nice have.

This project requires stretch OS on Raspberry Pi.
WEBIOPI setup on the RPi.
http://webiopi.trouch.com/

In WEBIOPI I set the startup config file to enable the GPIO's I'm using to output so each time the RPi starts up the GPIO's will be accessible. You can change the GPIO's or use the same in the Python scripts.

The Pool Controller works like this, when you click to change a mode it will turn off the pump before turning any valves as this is safer with my pump configuration. After the pump is off the modes will start changing and you will see the current mode turining off and the new mode turning on.

