from aaaabottle import Bottle, route, abort, template
import simplejson as json

app = Bottle()

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return json.dumps({'tasks': tasks})


@app.route('/api/v1.0/task/<task_id:int>')
def get_task2(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        raise HTTPError('data not found on Server')
    return json.dumps({'task': task[0]})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)
