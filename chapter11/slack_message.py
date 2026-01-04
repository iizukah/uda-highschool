# Slackにメッセージを送信

# ライブラリのインポート
from slack_sdk import WebClient

# トークンの設定
ACCESS_TOKEN = ""

# チャンネルIDの設定
CHANNEL = ""

# メッセージ
MESSAGE = "こんにちは"

# メッセージ送信の準備
client = WebClient(token = ACCESS_TOKEN)

# メッセージの送信
client.chat_postMessage(
    channel = CHANNEL,
    text = MESSAGE
)