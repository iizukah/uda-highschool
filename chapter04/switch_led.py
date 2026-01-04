import time
import RPi.GPIO as GPIO
PIN1, PIN2 = 4, 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        sw_status = GPIO.input(PIN2)

        #画面出力
        if sw_status == 0:
            GPIO.output(PIN1, GPIO.HIGH)
            print('スイッチON!')
        else:
            GPIO.output(PIN1, GPIO.LOW)
            print('')
        time.sleep(0.3) 
except KeyboardInterrupt:
    GPIO.cleanup()
