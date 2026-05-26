from flask import Blueprint,render_template,request,redirect,url_for



tasks_bp = Blueprint('tasks',__name__,template_folder='templates')

tasks_db = [
    {'id':1,'title':'купить хлеб','description':'успеть до закрытия'},
    {'id':2,'title':'сесть за комп','description':'успеть до того как уснешь'},
    {'id':3,'title':'поиграть в игру','description':'как нибуьдбь'},
    {'id':4,'title':'покушать','description':'если проглодался'},
]


@tasks_bp.route('/')
def get_all_tasks():
    return render_template('tasks.html', tasks_db=tasks_db)


@tasks_bp.route('/task/<int:id>')
def show_task(id):
    task_one = []

    for task in tasks_db:
        if task.get('id') == id:
            task_one.append(task)

    return render_template('detail.html',task_one=task_one)



@tasks_bp.route('/add',methods=['GET','POST'])
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        tasks_db.append({'id':len(tasks_db)+1, 'title':title, 'description':description})
        return redirect(url_for('tasks.get_all_tasks'))

    return render_template('add_task.html')