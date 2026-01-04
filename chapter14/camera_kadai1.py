# シャッター音を鳴らして写真を撮影しディスプレイに撮影した画像を表示させるプログラム

# ライブラリのインポート
import subprocess

# 画像ファイル名
image_file = "/home/pi/camera2.jpg"

# 撮影コマンド
command = "libcamera-still -n -o " + image_file

# コマンド実行
subprocess.call(command, shell=True)

# 音声ファイル名
wavfile = "/home/pi/shutter.wav"

# aplayコマンド
aplay_command = "aplay " + wavfile

# aplayコマンドの実行
subprocess.call(aplay_command, shell=True)

# 画像表示コマンド
command = "gpicview " + image_file

# コマンド実行
subprocess.call(command, shell=True)