# メール送信プログラム

# ライブラリのインポート
import smtplib
from email.utils import formatdate
from email.mime.text import MIMEText

# SMTPサーバー設定
SMTP_SERVER = "www.wincloud.site"
PORT_NUMBER = 587

# メール送信先
mail_to = "udhqoq@1t-ml.com"

# メール送信元
mail_from = "students@wincloud.site"

# 件名
subject = "RaspberryPiからメールが届きました。"

# 本文
body = "IoT講座を頑張りましょう"

# テキストのみのメール作成
msg = MIMEText(body, "plain")

# メールヘッダーに設定
msg["From"] = mail_from
msg["To"] = mail_to
msg["Date"] = formatdate()
msg["Subject"] = subject

# smtpサーバーから送信 
smtp_obj = smtplib.SMTP(SMTP_SERVER, PORT_NUMBER)
smtp_obj.ehlo()
smtp_obj.login("students", "winstudents")
smtp_obj.sendmail(mail_from, mail_to, msg.as_string())
smtp_obj.close()