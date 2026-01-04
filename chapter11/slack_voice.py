import subprocess
from slack_read import get_message

wavfile = "./slack.wav"
textfile = "./slack_voice.txt"
chown_command = "sudo chown pi:pi " + wavfile
aplay_command = "aplay " + wavfile

command = "sudo open_jtalk "
command += " -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice"
command += " -x /var/lib/mecab/dic/open-jtalk/naist-jdic "
command += " -ow " + wavfile
command += " " + textfile

with open(textfile, "w") as f:
	print(get_message(), file=f)

subprocess.call(command, shell=True)
subprocess.call(chown_command, shell=True)
subprocess.call(aplay_command, shell=True)
