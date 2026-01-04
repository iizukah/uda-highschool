# 写真を撮影しディスプレイに撮影した画像を表示させるプログラム

# ライブラリのインポート
import subprocess

# 画像ファイル名
image_file = "./camera2.jpg"

# 撮影コマンド
command = "libcamera-still -n -o " + image_file

# コマンド実行
subprocess.call(command, shell=True)

# 画像表示コマンド
command = "gpicview " + image_file

# コマンド実行
subprocess.call(command, shell=True)