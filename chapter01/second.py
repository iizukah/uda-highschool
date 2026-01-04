# -*- coding:utf-8 -*-

# 音声出力後、LEDランプを5回点灯させるプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time
import subprocess

# 音声ファイル名
wavfile = "/home/pi/first.wav"

# aplayコマンド
aplay_command = "aplay " + wavfile

# aplayコマンドの実行
subprocess.call(aplay_command, shell=True)

# GPIOピン番号
PIN = 4

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの4番を出力として使用
GPIO.setup(PIN, GPIO.OUT)

while True:
    message = input("何か入力(ON:点灯, OFF:消灯, EXIT: 終了): ")
    if message == "ON":
        GPIO.output(PIN, GPIO.HIGH)
    elif message == "OFF":
        GPIO.output(PIN, GPIO.LOW)
    elif message == "EXIT":
        break
    else:
        print("えらー！")


# GPIOピンの開放
GPIO.cleanup()
