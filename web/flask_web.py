# -*- coding:utf-8 -*-

import pymysql as mysql

import json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


db = mysql.connect(user='root',passwd='123456',db='JS',charset='utf8')
db.autocommit(True)


cursor = db.cursor()


@app.route('/',methods=['GET','POST'])
def hello():
    sql = ''
    if request.method == 'POST':
        data = request.json
        try:
            sql = "insert into js_infos(last_price) values(%s)" % (data['last_price'])
            ret = cursor.execute(sql)
        except mysql.IntegrityError:
            pass
        return "OK"

    else:
        cursor.execute('select last_price from js_infos ')
        ones = [[i[0]*1000,i[1]] for i in cursor.fetchall()]
        print(ones)
        return render_template('mom.html',data=json.dumps(ones))






@app.route('/new',methods=['GET'])
def getnew():
    cursor.execute('select last_price from js_infos')
    v = cursor.fetchall()

    return jsonify({'results': v})
    # return render_template('mom.html',data=json.dumps(v))



if __name__ == '__main__':
    app.run(port=8888,debug=True)


# 1. 从数据库抓数据是需要在视图函数中体现即可！ 但是需要几个瓶颈：
# 2. 返回的必须是json格式，如果满足？是要对数据库中的部分进行处理吗？ mongodb不是更容易实现？
# 3. 返回的数据如何与前端进行交互？满足数据可视化的需求！