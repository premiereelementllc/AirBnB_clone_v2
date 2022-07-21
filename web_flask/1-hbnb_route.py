#!/usr/bin/python3
""" start flask with Hello HBNB displayed """ 

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def disp_1():
	'''display the return'''
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def distp_2():
	''' display the return '''
	return "HBNB"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='5000')