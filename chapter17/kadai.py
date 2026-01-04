# 防犯システムプログラム

# ライブラリのインポート
import RPi.GPIO as GPIO
import time
import subprocess
import pexpect
from slack_sdk import WebClient
import smtplib
from email import encoders
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# GPIOピン番号
PIN = 14

# GPIOピンの指定方法
GPIO.setmode(GPIO.BCM)

# GPIOの14番を入力として使用
GPIO.setup(PIN, GPIO.IN)

# 今回は無限ループを使用しているので、
# キーボードで止めても、GPIOピンを解放するよう例外処理を入れる
try:
    # センサーが感知されるまで1秒ずつチェック(無限ループ）
    while True:
        if (GPIO.input(PIN) == GPIO.HIGH):
            print("センサーが人間を感知しました")
            break

        print("センサー感知中")
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    # GPIOピンの解放
    GPIO.cleanup()

# 写真を撮影する
image_file = "./capture.jpg"

# 撮影コマンド
image_command = "libcamera-still -n -t 1000 -q 10 -o " + image_file

# コマンド実行
subprocess.call(image_command, shell=True)


# アラーム音ファイル
wavfile = "./alert.wav"

# aplayコマンド
command = "aplay " + wavfile

# コマンド実行
subprocess.call(command, shell=True)

# 音声ファイル名
wavfile = "./security.wav"

# aplayコマンド
command = "aplay " + wavfile

# コマンド実行
subprocess.call(command, shell=True)

# サーバー設定
ID = 'students'
PASSWORD = 'winstudents'
HOST = 'www.wincloud.site'
DIR = 'public_html'

# 受講生ディレクトリ(ご自身の受講番号に変更してください)
students_dir = 'IoTiizuka/images'

# ローカルのファイル名
local_filename = 'capture.jpg'

# ファイル名
server_filename = 'capture.jpg'

# scpコマンド
scp_command = 'scp ' + local_filename
scp_command = scp_command + ' ' + ID + '@' + HOST + ':' + DIR + '/' + students_dir + '/' + server_filename

# コマンド実行
command = pexpect.spawn(scp_command)
command.expect('(?i)password')
command.sendline(PASSWORD)
command.expect(pexpect.EOF)

# トークンの設定
ACCESS_TOKEN = "xoxb-10123589857875-10219025600386-Myn6XqthR2qCtbGUjrlJuQ7l"

# チャンネルIDの設定
CHANNEL = "C0A3CFP54HM"

# メッセージ
MESSAGE = "防犯システムが作動しました。\n 写真URL：http://" + HOST + "/~students/" + students_dir + "/" + server_filename

# メッセージ送信の準備
client = WebClient(token = ACCESS_TOKEN)

# メッセージの送信
client.files_upload_v2(
    channel = CHANNEL,
    file = "capture.jpg",
    initial_comment = MESSAGE
)

# SMTPサーバー設定
SMTP_SERVER = "www.wincloud.site"
PORT_NUMBER = 587

# メール送信先
mail_to="lltjjd@1t-ml.com"

# メール送信元
mail_from = "students@wincloud.site"

# 件名
subject = "防犯システムが作動しました"

# 本文
body = "下記のURLから写真を確認してください。\n"
body = body + "http://"  + HOST + "/~students/" + students_dir + "/" + server_filename

# テキストのみのメール作成
msg = MIMEText(body, "plain")

# メールヘッダーに設定
msg["From"] = mail_from
msg["To"] = mail_to
msg["Date"] = formatdate()
msg["Subject"] = subject

# smptサーバーから送信 
smtp_obj = smtplib.SMTP(SMTP_SERVER, PORT_NUMBER)
smtp_obj.ehlo()
smtp_obj.login("students", "winstudents")
smtp_obj.sendmail(mail_from, mail_to, msg.as_string())
smtp_obj.close()
