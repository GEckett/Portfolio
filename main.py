from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(template_name_or_list="index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
