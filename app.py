from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config.from_object('config.Config')

tasks = [
    {'id': 1, 'title': 'Learn Flask', 'description': 'Understand how Flask works.', 'status': 'Pending'},
    {'id': 2, 'title': 'Build a To-Do App', 'description': 'Create a full-fledged To-Do application.', 'status': 'In Progress'}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_id = len(tasks) + 1
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        
        if title and description:
            tasks.append({'id': new_id, 'title': title, 'description': description, 'status': status})
            flash('Task added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Title and description are required!', 'danger')

    return render_template('task_form.html', task=None)

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if request.method == 'POST' and task:
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        task['status'] = request.form['status']
        flash('Task updated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('task_form.html', task=task)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
