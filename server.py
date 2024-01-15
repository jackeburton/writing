from flask import Flask, request, render_template
import threading, datetime

LENGTH_LIMIT = 10_000
TIME_LIMIT = 5

app = Flask(__name__)

@app.route('/')
def app_home_page():
    return render_template('app.html')

@app.route('/hello')
def hello():
    return 'hello from htmx'

@app.route('/post', methods=['GET','POST'])
def post():
    # print(request.form)
    return handler(request)
 

def handler(input):
    if input.content_length > LENGTH_LIMIT:
        print('length limit reached')
        return false
    input_text = request.form.get('text_box') 
    # start a timer, if after TIME_LIMIT seconds this code is not called again do another fucntion
    timer = threading.Timer(TIME_LIMIT, lambda: on_timeout(input_text))
    timer.start()
    file_name = str(datetime.datetime.now())
    file = open(file_name + '.txt', 'x')
    file.write(input_text)
    file.close()
    return render_template('text_box.html')

def on_timeout(post_text):
    print(f"has timedout: {post_text}")
    # clear the text area

if __name__ == '__main__':
    app.run(debug=True)
