from flask import Flask, render_template, request, redirect
from plot import make_plot 
import os 
import pandas as pd 
from bokeh.plotting import figure  
import json
from bokeh.embed import json_item
from jinja2 import Template 
from bokeh.resources import CDN

app = Flask(__name__)

html_page = os.path.join(os.getcwd(), 'templates', 'result.html')
page = Template(open(html_page, 'r').read())

@app.route('/')
def root(): 
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/home')
def home():
  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  if request.method == 'POST':
    ticker = request.form['ticker'].upper()
    price_type = request.form['price_type'] 		

    if ticker == '' or price_type == '':
      message = 'Please enter required fields.'
      return render_template('index.html', message=message)
    else:
      try: 
        p = make_plot(ticker, price_type) 
        with open('temp.txt', 'w') as f:
          f.write(f"{ticker},{price_type}")
        return page.render(resources=CDN.render())
      except:
        message = 'Please enter a valid ticker.'
        return render_template('index.html', message=message)       

@app.route('/plot')
def plot():
	with open('temp.txt', 'r') as f:
		ticker, price_type = f.read().split(',')	
	os.remove('temp.txt')

	p = make_plot(ticker, price_type) 
	return json.dumps( json_item(p, "myplot") )

if __name__ == '__main__':
  # app.debug = False
  app.run()
