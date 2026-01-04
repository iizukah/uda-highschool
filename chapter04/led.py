# LEDランプを5回点灯させるプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time

# GPIOピン番号
PIN = 4

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの4番を出力として使用
GPIO.setup(PIN, GPIO.OUT)

# LEDランプ5回点灯
for i in range(5):
    # 点灯
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(1)

    # 消灯
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(1)

# GPIOピンの解放
GPIO.cleanup()