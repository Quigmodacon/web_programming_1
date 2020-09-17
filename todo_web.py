import os
import sqlite3

from bottle import get, post, run, template, request, redirect

from bottle import default_app

@get('/')
def get_show_list():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return template("show_list", rows=result)


@get('/environ')
def get_environ():
    return os.environ


@get('/new_item')
def get_new_item():
    return template("new_item")


@post('/new_item')
def post_new_item():
    new_item = request.forms.get("new_item").strip()
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("insert into todo (task, status) values (?, ?)", (new_item, 1))
    conn.commit()
    cursor.close()
    redirect('/')


application = default_app()
#run(host="localhost", port=8080)