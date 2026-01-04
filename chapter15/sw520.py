import RPi.GPIO as GPIO
import time

PIN = 4  # SW-520 を接続した GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

try:
    while True:
        val = GPIO.input(PIN)

        if val == GPIO.LOW:
            print("振動を検知しました")
        else:
            print("振動なし")

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
