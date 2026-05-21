from flask import Blueprint,render_template



task_bp = Blueprint('tasks',__name__,template_folder='templates')

tasks_db = [
    {'id':1,'title':'купить хлеб','description':'успеть до закрытия'},
    {'id':2,'title':'сесть за комп','description':'успеть до того как уснешь'},
    {'id':3,'title':'поиграть в игру','description':'как нибуьдбь'},
    {'id':4,'title':'покушать','description':'если проглодался'},
]


@task_bp.route('/')
def get_all_tasks():
    return render_template('tasks.html', tasks_db=tasks_db)


@task_bp.route('/task/<int:id>')
def show_task(id):
    task_one = []

    for task in tasks_db:
        if task.get('id') == id:
            task_one.append(task)

    return render_template('detail.html',task_one=task_one)