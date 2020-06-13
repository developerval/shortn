from flask import Flask, make_response, jsonify, render_template, request, redirect
from linkgenerator import generate_link

app = Flask(__name__)

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
        return link_not_found(404)

@app.errorhandler(404)
def link_not_found(e):
    return render_template("link_404.html"), 404


if __name__ == '__main__':
    app.debug = False
    app.run()