from slack_sdk import WebClient

ACCESS_TOKEN = ""
CHANNEL = ""
client = WebClient(token = ACCESS_TOKEN)

def get_message():
  response = client.conversations_history(channel=CHANNEL)
  message = response["messages"][0]["text"].replace("\n", "")
  return message

if __name__ == "__main__":
  print(get_message())