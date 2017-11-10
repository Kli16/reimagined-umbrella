from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)

@my_app.route('/')
def root():
    u = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=XL14uyV1V926vFejFjhsr5D2N11DQaQ8zcuUJjmb')
    data = u.read()
    nasa_stuff = json.loads(data)
    return render_template('index.html', info = nasa_stuff)

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
