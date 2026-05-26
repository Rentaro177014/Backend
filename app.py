from flask import Flask,jsonify

from toDO.routes import tasks_bp

app = Flask(__name__)


app.register_blueprint(tasks_bp,url_prefix='/tasks')


@app.route('/')
def main():
    return 'главная страница'


@app.route('/posts')
def postes():
    return 




@app.route('/add_post')
def add_post():
    return



@app.route('/add_post/<id>')
def view_id():
    return id


if __name__ == '__main__':
    app.run(debug=True)

