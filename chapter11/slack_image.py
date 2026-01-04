# Slackに画像を送信

# ライブラリのインポート
from slack_sdk import WebClient

# トークンの設定
ACCESS_TOKEN = ""

# チャンネルIDの設定
CHANNEL = ""

# メッセージ
MESSAGE = "画像を送ります"

# メッセージ送信の準備
client = WebClient(token = ACCESS_TOKEN)

# 画像とメッセージの送信
client.files_upload_v2(
    channel = CHANNEL,
    file = "cat.jpg",
    initial_comment = MESSAGE
)
