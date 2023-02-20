
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cards = cur.execute('SELECT * FROM card').fetchall()
    conn.close()
    return render_template('index.html',cards=cards)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/selectcard')
def list_cards():
    id = request.args.get('id')
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    card = cur.execute('SELECT * FROM card WHERE cardid =' + str(id)).fetchone()
    conn.close()
    return render_template('card.html', card=card)

@app.route('/wish')
def wish_form():
    id = request.args.get('id')
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    card = cur.execute('SELECT * FROM card WHERE cardid =' + str(id)).fetchone()
    conn.close()
    return render_template('form_wish.html', card=card)


@app.route('/wish_insert', methods=['POST'])
def wish_insert():
    sender = request.form.get("sender")
    message = request.form.get("message")
    cardid = request.form.get("id")

    letters = string.ascii_lowercase
    generated_id = ''.join(random.choice(letters) for i in range(10))
    while cur.execute('SELECT genid FROM wish WHERE genid =' + str(generated_id)).fetchone() is None:
        generated_id = ''.join(random.choice(letters) for i in range(10))

    # connect and open the database file database.db
    conn = sqlite3.connect('database.db')
    conn.execute("INSERT INTO wish (sender, message, cardid) VALUES ('" + sender + "', '" + message + "', '" + cardid + "')")
    # commit the new row to the database, otherwise it will be lost
    conn.commit()
    # close the connection
    conn.close()
    return render_template('wish_confirm.html',generated_id=generated_id)


# ----------------------------------------------------------------------------------------------------------------------
# brent read wish:
@app.route('/wish_reader')
def message_reader():
    return render_template('wish_reader.html')


@app.route('/submit_read_wish', methods=['POST'])
def read_wish():
    id_wish = request.form.get("code")
    # connect and open the database file database.db
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    wish = cur.execute('SELECT * FROM wish where wishid=' + str(id_wish)).fetchall()
    conn.close()
    return render_template('read_wish.html', wish=wish)
# ----------------------------------------------------------------------------------------------------------------------

