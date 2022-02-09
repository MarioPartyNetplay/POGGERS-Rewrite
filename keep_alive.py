#***************************************************************************#
#                                                                           #
# Doopliss - A Discord Bot For Me.                                          #
# https://github.com/NoraHanegan/Doopliss                                   #
# Copyright (C) 2021 Nora Hanegan. All rights reserved.                     #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I am not dead."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()