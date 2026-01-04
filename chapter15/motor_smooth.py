import RPi.GPIO as GPIO
import time

PIN = 4
freq = 50  # サーボ用PWM周波数

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

pwm = GPIO.PWM(PIN, freq)
pwm.start(0)

def set_angle(angle):
    duty = 2.5 + (angle / 18)
    pwm.ChangeDutyCycle(duty)

def smooth_move(start, end, step=1, delay=0.02):
    """start→end を step°ずつ delay秒ごとに動かす"""
    if start < end:
        rng = range(start, end + 1, step)
    else:
        rng = range(start, end - 1, -step)

    for angle in rng:
        set_angle(angle)
        time.sleep(delay)

try:
    while True:
        print("0° → 180°")
        smooth_move(0, 180, step=1, delay=0.02)

        time.sleep(0.5)

        print("180° → 0°")
        smooth_move(180, 0, step=1, delay=0.02)

        time.sleep(0.5)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()