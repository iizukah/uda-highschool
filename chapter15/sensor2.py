import RPi.GPIO as GPIO
import time

PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

time.sleep(2)  # センサー安定待ち

try:
    for _ in range(60):
        if GPIO.input(PIN):
            print("人体を感知しました")
        else:
            print("人体を感知していません")
        time.sleep(1)

finally:
    GPIO.cleanup()