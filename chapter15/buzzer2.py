import RPi.GPIO as GPIO
import time

BUZZER_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 周波数は 440Hz（ラの音）に設定
pwm = GPIO.PWM(BUZZER_PIN, 440)
pwm.start(0)  # 最初は無音

# デューティ比のリスト（音量）
duty_list = [0, 10, 50, 100]

try:
    for duty in duty_list:
        print(f"Duty = {duty}%")
        pwm.ChangeDutyCycle(duty)
        time.sleep(1)  # 1秒ずつ鳴らす

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()