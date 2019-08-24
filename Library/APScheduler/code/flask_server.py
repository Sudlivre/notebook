import json

from flask import Flask, request, jsonify
from flask_restful import Api, Resource

from timed_manager import TimedTaskManager
from timed_method import print_task, spider_task, process_task


app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    data = [
        {'name': 'zhangsan', 'age': 14},
        {'name': 'lisi', 'age': 15},
        {'name': 'wanger', 'age': 16},
        {'name': 'xiaosan', 'age': 17}
    ]
    return jsonify({'result': 'success', 'data': data})


@app.route('/api/print')
def timed_print():
    res = TimedTaskManager().add_default_job(print_task)
    return jsonify({'result': 'success'})


@app.route('/api/spider')
def timed_spider():
    res = TimedTaskManager().add_cron_job(spider_task, minute='*/5')
    return jsonify({'result': 'success'})


@app.route('/api/process')
def timed_process():
    res = TimedTaskManager().add_cron_job(process_task, minute='*/10')
    return jsonify({'result': 'success'})


@app.route('/api/scheduler')
def timed_scheduler():
    res = TimedTaskManager().start_scheduler()
    return jsonify({'result': 'success'})


@app.route('/api/turn_off_scheduler')
def turn_off_scheduler():
    res = TimedTaskManager().shutdown_scheduler()
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
