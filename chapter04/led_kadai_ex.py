# LEDランプを10回点灯させるプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time

# GPIOピン番号
PIN1 = 4
PIN2 = 10

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの4, 10番を出力として使用
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)

# LEDランプ10回点灯
for i in range(10):
    # 4点灯, 10消灯
    GPIO.output(PIN1, GPIO.HIGH)
    GPIO.output(PIN2, GPIO.LOW)
    time.sleep(1)

    # 4消灯, 10点灯
    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN2, GPIO.HIGH)
    time.sleep(1)

# GPIOピンの解放
GPIO.cleanup()
