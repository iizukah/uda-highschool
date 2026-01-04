import subprocess

wavfile = "/home/pi/hello.wav"
textfile = "/home/pi/voice_sample.txt"

command = [
    "sudo", "open_jtalk",
    "-m", "/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice",
    "-x", "/var/lib/mecab/dic/open-jtalk/naist-jdic",
    "-ow", wavfile,
    textfile
]

chown_command = ["sudo", "chown", "pi:pi", wavfile]

aplay_command = ["aplay", wavfile]

subprocess.call(command)
subprocess.call(chown_command)
subprocess.call(aplay_command)
