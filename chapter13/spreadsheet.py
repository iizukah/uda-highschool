import requests
import sys

arg = sys.argv[-1]
url = "https://script.google.com/macros/s/AKfycbzquAaHerYUjPlQc51RVykhj2s6hgg-HkTY1xx4070jufVEthRToTUShB6w-D95yy0K/exec"
params = {"name": "iizuka", "data1": arg, "data2": 0, "data3": 0, "data4": 0}

try:
  requests.get(url, params=params)
  print("ok")
except:
  pass
  print("error")