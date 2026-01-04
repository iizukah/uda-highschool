import RPi.GPIO as GPIO
import time

PIN = 4
freq = 50  # サーボ用PWM周波数（50Hz）

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

pwm = GPIO.PWM(PIN, freq)
pwm.start(0)

def set_angle(angle):
    duty = 2.5 + (angle / 18)  # 0°→2.5%, 180°→12.5%
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)

try:
    while True:
        set_angle(0)
        print("0度")
        time.sleep(1)

        set_angle(90)
        print("90度")
        time.sleep(1)

        set_angle(180)
        print("180度")
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()