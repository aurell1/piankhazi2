from flask import Flask
import os
import web

app = Flask(__name__)
render = web.template.render('templates/')

@app.route("/")
def my_func():

	return "Sikeres futas!"
	
class Index(object):
    def GET(self):
        form = web.input(name="Nobody")
        greeting = "Hello, %s" % form.name

        return render.index(greeting = greeting)
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=os.environ.get("PORT", None))
