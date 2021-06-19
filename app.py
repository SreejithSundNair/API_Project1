from flask import Flask, redirect, url_for
#### WebServerGatewayInterface--WSGI
app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to my first app"


@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The result is passed</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "<html><body><h1>The result is not passed</h1></body></html>"


@app.route('/results/<int:score>')
def results(score):
    result=""
    if score <50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=score))

if __name__ == '__main__':
    app.run(debug=True)