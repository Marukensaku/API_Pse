# coding:utf-8
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 这就是纯纯前端的问题了！
@app.route('/')
def index():
    return render_template('chart.html')


@app.route('/data')
def data():
    # sample 从指定序列中随机获取指定长度的片断，sample函数不会修改原有序列
    return jsonify({'results': random.sample(range(1, 10), 5)})


if __name__ == '__main__':
    app.run(debug=True)
