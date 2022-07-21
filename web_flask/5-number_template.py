#!/usr/bin/python3
''' add number display to template pages '''

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
        return "c {}".format(text).replace("_", " ")

@app.route('/python/', strict_slashes=False, defaults={'text': "is cool"})
@app.route('/python/(<text>)', strict_slashes=False)
def python_text(text):
        '''python file text tag'''
        return "python {}".format(text).replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def is_it_a_number(n):
        ''' output number if its a number '''
        return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_if_number(n):
	''' display html page if n is a number '''
	return render_template('5-number.html', n=n)

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000')
