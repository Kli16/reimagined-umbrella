from flask import Flask, render_template
import urllib2, json
import random

my_app = Flask(__name__)

@my_app.route('/')
def root():
    u = urllib2.urlopen('https://www.refugerestrooms.org/api/v1/restrooms.json?page=2&per_page=5&offset=2&ada=true&unisex=true')
    data = u.read()
    refugerestrooms = json.loads(data)
    return render_template('index.html', info = refugerestrooms[random.randint(0,3)])

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
