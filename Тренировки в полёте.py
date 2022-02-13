from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/<job>')
@app.route('/index<job>')
def index(job):
    return render_template('training.html', job=job)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
