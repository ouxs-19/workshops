from flask import Flask, render_template, request, render_template_string
import importlib
import os

app = Flask(__name__)

@app.context_processor
def add_imports():
    return dict(os=os)

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/generate')
def generate():
    if request.method == 'POST':
        n = int(request.form['number'])
        return render_template('generate.html', n=n)

@app.get('/render')
def vulnerable():
    print(request.args)
    template = request.args.get("tpl","")
    if template:
        return render_template_string(template)
    return "Please provide a tempalate"

if __name__ == '__main__':
    app.run(debug=True)