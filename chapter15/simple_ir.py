import RPi.GPIO as GPIO
import time

PIN = 21  # IR受信モジュールのOUTを接続

GPIO.setmode(GPIO.BCM)

# 内部プルアップを有効化
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("リモコンの信号を待っています...")

try:
    while True:
        if GPIO.input(PIN) == GPIO.LOW:  # 受信時は LOW
            print("赤外線信号を検知しました")
            time.sleep(0.2)  # チャタリング防止

        time.sleep(0.01)

except KeyboardInterrupt:
    print("\n終了します。")

finally:
    GPIO.cleanup()