from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup')
def signUp():
    return render_template('signup.html')
    
# @app.route('/details')
def details():
    return "flask for back end and vue.js for front end."

app.add_url_rule('/details', 'details', details)
if __name__ == '__main__':
    # app.run(host, port, debug, options)
    app.run(host='0.0.0.0', port=1210)