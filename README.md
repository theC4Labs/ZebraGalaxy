# ZebraGalaxy
The evolving code of the Zebra Galaxy LED board for Raspberry Pi

The Zebra Galaxy circuit board leverages a pure Python library for the APA102 RGB LED made by “tinue (Martin)” a Swiss programmer.  His excellent library leverages the Adafruit GPIO library.

Before beginning, make sure your Raspberry Pi is configured to use SPI.  That can be set in “rasp-config” under the advanced settings.  Then reboot.

For installation of the Galaxy, first setup the Adafruit GPIO libraries available here:

https://github.com/adafruit/Adafruit_Python_GPIO

Follow their instructions to set up the GPIO library.

We have included here the APA102 library as well as Martin’s test scripts.  If you want to separately get the latest version of his project you can find it here:

https://github.com/tinue/APA102_Pi

To activate the 18 LEDs, simply run the “Galaxy.py” script or the “runcolorcycle.py” to see a demo.

To run a script at startup, add the path to the end of the “/etc/r.local” file just before the “exit 0” line.

Example:     “sudo python /home/pi/Downloads/ZebraGalaxy-master/galaxy.py &”

To change the color and behavior of the LEDs, modify the script and reboot or kill the process and restart.
