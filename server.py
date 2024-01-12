from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def app_home_page():
    return render_template('app.html')

@app.route('/hello')
def hello():
    return 'hello from htmx'

if __name__ == '__main__':
    app.run(debug=True)
