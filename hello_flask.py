from flask import Flask, url_for, redirect, render_template, request, flash
import pymysql
import json

app = Flask(__name__)

@app.route('/para/<user>')
def index(user):
    return render_template('abc.html', user_template=user)

@app.route('/user/<username>')
def username(username):
    return 'I am ' + username

# <型別:參數>
@app.route('/age/<int:age>')
def userage(age):
    return 'I am ' + str(age) + ' years old'
    # return 'i am ' + age + ' years old'  #  故意造成型別錯誤

@app.route('/a')
def url_for_a():
    return 'here is a'

@app.route('/b')
def b():
    #  會將使用者引導到'/a'這個路由
    return redirect(url_for('url_for_a'))

"""
# 之前測驗不同路徑也可通到舊的路徑
@app.route('/loginurl', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if login_check(request.form['username'], request.form['password']):
            flash('Login Success!')
            return redirect(url_for('hello', username=request.form.get('username')))
    return render_template('login.html')
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('hello', username=request.form.get('username')))
    return render_template('login.html')
        
def login_check(username, password):
    """登入帳號密碼檢核"""
    if username == 'admin' and password == 'hello':
        return True
    else:
        return False

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)

@app.route('/data')
def data():
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='curry30', db='cai', charset='utf8')

    #使用cursor方法創建一個遊標
    cursor = db.cursor()
    
    #查詢數據庫版本
    cursor.execute("select version()")
    data = cursor.fetchone()
    # print(" Database Version:%s" % data)

    #查詢數據表數據
    sql = "select * from pk10 limit 10"
    cursor.execute(sql)
    data = cursor.fetchall()
    # print(data)

    # print(data) 
    for i in data:
        return i

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'Your Key'
    app.run()