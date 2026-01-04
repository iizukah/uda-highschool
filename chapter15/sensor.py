# 人体を感知したら、メッセージを表示するプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time

# GPIOピン番号
PIN = 4

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの4番を入力として使用
GPIO.setup(PIN, GPIO.IN)

# 1分間1秒ずつチェックしてメッセージを表示
for i in range(1, 61):
    if (GPIO.input(PIN) == GPIO.HIGH):
        print("人体を感知しました")

    else:
        print("人体を感知していません")

    time.sleep(1)

# GPIOピンの解放
GPIO.cleanup()
