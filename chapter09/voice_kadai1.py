# PythonからOpenJTalkを呼び出し音声を出力プログラム

# ライブラリのインポート
import subprocess

# 音声ファイル名
wavfile = "/home/pi/answer.wav"

# テキストファイル名
textfile = "/home/pi/kadai.txt"

# chownコマンド
chown_command = "sudo chown pi:pi " + wavfile

# aplayコマンド
aplay_command = "aplay " + wavfile

# OpenJTalkのコマンド
command = "sudo open_jtalk "
command = command + " -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice"
command = command + " -x /var/lib/mecab/dic/open-jtalk/naist-jdic "
command = command + " -ow " + wavfile
command = command + " " + textfile

# 音声ファイル作成
subprocess.call(command, shell=True)

# 作成したwavファイルの所有者をrootからpiに変更
subprocess.call(chown_command, shell=True)

# aplayコマンドの実行
subprocess.call(aplay_command, shell=True)
