# 人体を感知したら、メッセージとLEDを表示するプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time

# GPIOピン番号
PIN = 4
PIN2 = 14

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの4番を入力として使用
GPIO.setup(PIN, GPIO.IN)

# GPIOの14番を出力として使用
GPIO.setup(PIN2, GPIO.OUT)

# 1分間1秒ずつチェックしてメッセージを表示とLEDを点灯消灯させる
for i in range(1, 61):
    if (GPIO.input(PIN) == GPIO.HIGH):
        # 点灯
        print("人体を感知しました")
        GPIO.output(PIN2, GPIO.HIGH)
        time.sleep(1)

    else:
        # 消灯
        print("人体を感知していません")
        GPIO.output(PIN2, GPIO.LOW)
        time.sleep(1)

# GPIOピンの解放
GPIO.cleanup()