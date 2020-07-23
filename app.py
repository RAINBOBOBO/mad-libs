from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
debug = DebugToolbarExtension(app)

@app.route("/")
def generate_form():
	"""generate a form based on prompts in given story instance"""
	return render_template("questions.html", word_list=story.prompts)

@app.route("/story")
def generate_story():
	"""generate a story as a string from a form submission"""
	answers = {key: val for (key, val) in request.args.items() if key in story.prompts}

	final_text = story.generate(answers)
	return render_template("story.html", final_text=final_text)
