import iptrss.others.installerm as melloins
try:
    from flask import Flask
except:
    melloins.pip_install("flask")
    from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Hello, YourBot is alive!"
  
def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
