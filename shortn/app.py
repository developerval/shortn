from flask import Flask, make_response, jsonify, render_template, request, redirect
from link_utility import generate_link
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'shortn'
    id = db.Column(db.Integer, primary_key=True)
    original_ = db.Column(db.String())
    shortened_ = db.Column(db.String(5), unique=True)

    def __init__(self, original_, shortened_):
        self.original = original_
        self.shortened = shortened_


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/success', methods=['POST', 'GET'])
def success():
    req = request.get_json()
    print(req)

    newone = generate_link()

    res = make_response(jsonify(newone), 200)
    return res


@app.route('/<url>')
def forward(url):
    if url == 'OqSk7':
        return redirect('http://www.linkedin.com')
    else:
        return render_template("link_404.html")

# TODO: add actual 404 error page, also need to create the page in HTML


if __name__ == '__main__':
    app.debug = False
    app.run()
