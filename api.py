import os
import subprocess

from flask import Flask

root = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/')
def rapl():
    try:
        teste = int(subprocess.run([f'{root}/execpower.sh'], stdout=subprocess.PIPE).stdout.decode('utf-8'))
    except:
        teste = 2
    return {"powercap": teste}