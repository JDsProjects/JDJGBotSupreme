from flask import Flask
from threading import Thread
# import only system from os 
from os import system, name 
import clear_code

app = Flask('')

@app.route('/')
def home():
    return "Running 24/7..."

def run():
  app.run(host='0.0.0.0',port=8080)
  clear_code.clear()

def keep_alive():  
    t = Thread(target=run)
    t.start()
    clear_code.clear()