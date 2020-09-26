from flask import Flask, render_template, redirect, url_for, request
from collections import Counter

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello from Flask!'

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credntials.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html') 

@app.route('/countme/<input_str>')
def count_me(input_str):
	input_counter = Counter(input_str)
    	response = []
    	for letter, count in input_counter.most_common():
        	response.append('"{}": {}'.format(letter, count))
    	return '<br>'.join(response)


if __name__ == '__main__':
  app.run()

