import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED_PIN = 4
SW_PIN = 18

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 割り込み時に呼ばれる関数
def switch_callback(channel):
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("スイッチON!")
    time.sleep(5)
    GPIO.output(LED_PIN, GPIO.LOW)
    print("スイッチOFF")

GPIO.add_event_detect(SW_PIN, GPIO.RISING, callback=switch_callback, bouncetime=50)

try:
    print("割り込み待ち中...")
    while True:
        time.sleep(1) 
except KeyboardInterrupt:
    GPIO.cleanup()
