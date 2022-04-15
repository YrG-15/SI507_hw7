from flask import Flask,render_template
import requests
from secret import api_key

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/name/<nm>')
def name(nm):
	# name = 'Buffy'
	return render_template('name.html',name=nm)

@app.route('/headlines/<nm>')
def getheadlines(nm):
	url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key='+api_key
	results = requests.get(url).json()
	headlines = []
	for i in range(5):
		headlines.append(results['results'][i]['title'])
	return render_template('headlines.html',name=nm,headlines=headlines)

@app.route('/links/<nm>')
def getheadlineslink(nm):
	url = 'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key='+api_key
	results = requests.get(url).json()
	urls = []
	headlines = []
	for i in range(5):
		headlines.append(results['results'][i]['title'])
		urls.append(results['results'][i]['url'])
	return render_template('headlines_link.html',name=nm,headlines=headlines,urls= urls)

if __name__ == '__main__':
	print('starting Flask app',app.name)
	app.run(debug=True)
