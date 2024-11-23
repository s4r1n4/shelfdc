from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Your program is alive and running"

def run():
  app.run(host='0.0.0.0',port=3306)

def keep_alive():
    t = Thread(target=run)
    t.start()