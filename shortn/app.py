from flask import Flask, make_response, jsonify, render_template, request
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

if __name__ == '__main__':
    app.debug = True
    app.run()