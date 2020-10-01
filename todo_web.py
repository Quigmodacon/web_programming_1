import os
import sqlite3

from bottle import get, post, template, request, redirect

ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ.keys()

if ON_PYTHONANYWHERE:
    from bottle import default_app
else:
    from bottle import run, debug

@get('/')
def get_show_list():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return template("show_list", rows=result)





@get('/set_status/<id:int>/<value:int>')
def get_set_status(id, value):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("update todo set status=? where id=?", (value, id, ))
    conn.commit()
    cursor.close()
    redirect('/')


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


@get('/update_item/<id:int>')
def get_update_item(id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("select * from todo where id=?", (id,))
    result = cursor.fetchall()
    cursor.close()
    return template("update_item", row=result[0])


@post('/update_item')
def post_update_item():
    id = int(request.forms.get("id").strip())
    new_item = request.forms.get("updated_item").strip()
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("update todo set task=? where id=?", (updated_item, id))
    conn.commit()
    cursor.close()
    redirect('/')


@get('/delete_item/<id>')
def get_delete_item(id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("delete from todo where id=?", (id,))
    conn.commit()
    cursor.close()
    redirect('/')


if ON_PYTHONANYWHERE:
    application = default_app()
else:
    debug(True)
    run(host="localhost", port=8080)
