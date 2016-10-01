from flask import Flask
import os

app = Flask(__name__)

def my_func():
	return 'Sikeres futás!'
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=os.getenv('PORT', None)
	