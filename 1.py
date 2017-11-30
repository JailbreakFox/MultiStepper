#!/usr/bin/python  
import wiringpi  
#wiringpi.wiringPiSetupSys()  
#wiringpi.pinMode(25,1)  
#wiringpi.digitalWrite(25,1)  
  
#wiringpi.wiringPiSetup()  
#wiringpi.pinMode(6,1)  
#wiringpi.digitalWrite(6,1)  

wiringpi.wiringPiSetupGpio()  
while True:

	wiringpi.pinMode(25,1)  
	wiringpi.digitalWrite(25,1)  