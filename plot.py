import pandas as pd  
from bokeh.plotting import figure

def make_plot(ticker, price_type):
	apikey = "KAX4TFKXT0EZ4T70"
	full_price_name = {"open" : "Opening Price", 
					"high" : "Daily High", 
					"low"  : "Daily Low", 
					"close": "Closing Price", 
					"adjusted_close" : "Adjusted Closing Price"	
					}
	url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={apikey}&datatype=csv'
	df = pd.read_csv(url)

	TOOLS = "pan, wheel_zoom, box_zoom, reset, save" 
	p = figure(x_axis_type = 'datetime', tools = TOOLS, plot_width = 1000, title = "{}'s Historical {}".format(ticker, full_price_name[price_type])) 
	p.line(pd.to_datetime(df.timestamp), df[price_type] ) 

	return p