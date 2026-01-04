# LEDランプを10回点灯させるプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time

# GPIOピン番号
PIN = 10

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの10番を出力として使用
GPIO.setup(PIN, GPIO.OUT)

# LEDランプ10回点灯
for i in range(10):
    # 点灯
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(0.1)

    # 消灯
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(0.1)

# GPIOピンの解放
GPIO.cleanup()
