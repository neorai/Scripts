#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import subprocess
import MySQLdb

btn1 = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def buttonPress():
  btn1_input = GPIO.input(btn1)
  return btn1_input

def button_callback(channel):
	
	start = time.time()
    	stop = 0

	while buttonPress() == False:
		time.sleep(1)
		stop = time.time()
		if stop == 0:
			pass
		else:
			duration = (stop - start)
			print "%s boton pulsado" % (duration)
			if duration > 5 and duration < 6:
				print 'llevas 5 segundos pulsando, mensaje a telegram enviado'
				
				cnx = MySQLdb.connect( '192.168.1.195', 'root', 'root', 'raspberry')
				cursor = cnx.cursor()

				estado_puerta = ("INSERT INTO puertas (puerta, estado) VALUES (%s, %s)")
				datos_puerta = ('calle','1')

				cursor.execute(estado_puerta,datos_puerta)

				cnx.commit()

				cursor.close()
				cnx.close()
	start = time.time()
    	stop = 0

	while buttonPress() == True:
		time.sleep(1)
		stop = time.time()
		if stop == 0:
			pass
		else:
			duration = (stop - start)
			print "%s boton no pulsado" % (duration)
			duration_int = int(duration)
			if (duration_int % 5 == 0) or (duration_int == 1) :
				cnx = MySQLdb.connect( '192.168.1.195', 'root', 'root', 'raspberry')
				cursor = cnx.cursor()

				estado_puerta = ("INSERT INTO puertas (puerta, estado) VALUES (%s, %s)")
				datos_puerta = ('calle','0')

				cursor.execute(estado_puerta,datos_puerta)

				cnx.commit()

				cursor.close()
				cnx.close()
		
	
GPIO.add_event_detect(btn1, GPIO.FALLING,  callback=button_callback, bouncetime=100)

try:
	while True:
		time.sleep(1)
		pass

except KeyboardInterrupt:
	GPIO.cleanup()
