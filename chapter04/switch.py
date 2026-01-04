import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
PIN = 18
#GPIO18を入力端子設定
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    sw_status = GPIO.input(PIN)

    if sw_status == 0:
        print('スイッチON!')
    else:
        print('')

    time.sleep(0.3) 
