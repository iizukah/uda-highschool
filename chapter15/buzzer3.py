import RPi.GPIO as GPIO
import time

BUZZER_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# PWM（パッシブブザー用）
pwm = GPIO.PWM(BUZZER_PIN, 440)  # 初期周波数は適当でOK
pwm.start(50)  # デューティ比50%

# 音階の周波数（ドレミファソラシド）
notes = [
    262,  # ド
    349,  # ファ
    494,  # シ
]

try:
    for freq in notes:
        print(f"freq = {freq} Hz")
        pwm.ChangeFrequency(freq)
        time.sleep(1)  # 音の長さ

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()