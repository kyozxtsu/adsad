from flask import Flask, render_template, request
import pymysql
app = Flask(__name__)


@app.route('/')
def main():
    return render_template("feedback.html")


@app.route('/', methods=['POST'])
def main1():
    print(request.form)
    connect = pymysql.connect(host='localhost', port='', user='', password='', db='')

    table = "CREATE TABLE IF NOT EXISTS support (name VARCHAR(255), email VARCHAR(255), message VARCHAR(1024))"
    with connect.cursor() as cur:
        cur.execute(table)
        ins = f"INSERT INTO support (name, email, message) VALUES (%s, %s, %s)"
        val = (request.form['name'], request.form['email'], request.form['message'])
        cur.execute(ins, val)
        connect.commit()


    return render_template("feedback.html")



app.run()