from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index(username=None):
    return render_template('index.html', username='Mike')

if __name__ == "__main__":
    app.debug = True
    app.run()
