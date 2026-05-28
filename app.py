from flask import Flask,jsonify

from toDO.routes import tasks_bp

from database.engine import db
from database.models.todo import Task
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


with app.app_context():
    db.create_all()




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

