import os
import time
import RPi.GPIO as GPIO

#Change this to whatever temperature you want the fan to kick on at.
#https://github.com/andrewkarch/Eleduino-Fan-Controller
#sudo nano /etc/rc.local
#sudo python /home/pi/fan/fanController.py &
maxTemp = 45 #Celsius
#Sets the time to wait in between checks
waitTime = 10 #seconds

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)
while(True):
    temperature = os.popen('vcgencmd measure_temp').readline()
    tempInC = float(temperature.replace("temp=","").replace("'C\n",""))
    if(tempInC >= maxTemp):
        GPIO.output(3, True)
    else:
        GPIO.output(3, False)
    time.sleep(waitTime)
	