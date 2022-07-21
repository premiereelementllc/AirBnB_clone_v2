#!/usr/bin/python3
''' start a flask diplay 3 '''

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

@app.route('/c/<text>', strict_slashes=False)
def replace_ctext(text):
        ''' inputs '''
        return "c {}".format(text.replace("_", " "))

@app.route('/python/', strict_slashes=False, defaults={'text': "is cool"}}
@app.route('/python/(<text>)', strict_slashes=False)
def python_text(text):
	'''python file text tag'''
	return "python {}".format(text.replace("_", " "))

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')
