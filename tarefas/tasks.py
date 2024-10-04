from celery import Celery

#app = Celery('tasks', broker='redis://172.19.0.2:6379/0')
app = Celery('hello', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y