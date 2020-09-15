from bottle import get, post, run, template, request, redirect
import sqlite3

@get('/')
def get_show_list():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return template("show_list", rows=result)

@get('/new_item')
def get_new_item():
    return template("new_item")

@post('/new_item')
def post_new_item():
    new_item = request.form.get("new_item").strip()
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("insert into todo (task, status) values (?, ?)", (new_item, 1))
    conn.commit()
    cursor.close()
    redirect('/')

run(host="localhost", port=8080)