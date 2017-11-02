from flask import Flask, render_template, flash, redirect
from forms import AddRiskForm, AddReviewForm
import addrisk
import sqlite3

app = Flask(__name__)
app.config.from_object('config')
db_filename = 'addrisk.db' #Created by db_initialize.py

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ryan'}  # To greet you at top of page
    posts = []

    with sqlite3.connect(db_filename) as conn: #connect to db and pull reviews
        cursor = conn.cursor()
        cursor.execute("""
        select nickname, review from reviews
        """)

        for row in cursor.fetchall():
            nickname, review = row
            posts.append({
                'author': {'nickname': nickname},
                'body': {'review': review}
            })

    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)

@app.route('/addrisks', methods=['GET', 'POST'])
def addrisks():
    user = {'nickname': 'Ryan'}  # To greet you at top of page
    form = AddRiskForm()
    if form.validate_on_submit(): #Do if form is filled out

        flash('Added Risk to OrderID="%s"' % (form.orderid.data))

        ordertoaddrisk = form.orderid.data
        addrisk.editorder(ordertoaddrisk)

        return redirect('/index')
    return render_template('addrisks.html',
                            title='Add Risk',
                            user=user,
                            form=form)

@app.route('/addreview', methods=['GET', 'POST'])
def addreview():
    user = {'nickname': 'Ryan'}  # To greet you at top of page
    form = AddReviewForm()
    if form.validate_on_submit(): #Do if form is filled out

        flash('Added Review from "%s"' % (form.nickname.data))

        with sqlite3.connect(db_filename) as conn: #connect to db add review
            cursor = conn.cursor()
            cursor.execute("INSERT INTO reviews (nickname, review) VALUES (?, ?)",
                            (form.nickname.data, form.review.data))

        return redirect('/index')
    return render_template('addreview.html',
                            title='Add Review',
                            user=user,
                            form=form)