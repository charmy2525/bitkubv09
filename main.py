# [START gae_python37_app]
from flask import Flask
from bitkub import Bitkub

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

API_KEY = '04c859241ce7cb77c2c6e8ef9f7481bf'
API_SECRET = '2b6833f376de370834538c00a38b756f'

# initial obj non-secure and secure
bitkub = Bitkub(api_key=API_KEY, api_secret=API_SECRET)
import requests
url = 'https://notify-api.line.me/api/notify'
token = 'HG7VEAzCskajzj8OLJ1dMmAwYvuBWmMXMOhFKjZS0Tn'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
import time
start = 1593702012.6649423


@app.route('/')
def hello():
    j = 1
    while j < 200:  
        zrx=bitkub.ticker(sym='THB_ZRX')
        x = zrx.get('THB_ZRX')
        last=x.get('last')
        msg = last
        r = requests.post(url, headers=headers, data = {'message':msg})
        #print (r.text)
        #seconds = int(time.time()-start) % 60
        #sleeptime = 60 - seconds
        #time.sleep(sleeptime)
    return r.text


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
