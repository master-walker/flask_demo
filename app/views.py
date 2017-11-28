#!/usr/bin/env python
#coding=utf-8


from app import app
from flask import render_template, flash,redirect, request, make_response, session,url_for
from .forms import LoginForm, FormDemo
from datetime import datetime
from database import db, User

@app.route("/")
def index():
    user = {"nickname": "baby"}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title="test flask web app",user=user,posts=posts)


@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("login requested for openid='" + form.openid.data + "', remember_me=" + form.remember_me.data)
        redirect("/index")
    return render_template("login.html",title="Sign in",form=form)


@app.route("/test")
def test():
    user_agent = request.headers.get('User-Agent')
    # response = make_response("<p>the document carrie cookie</p>")
    # response.set_cookie("answer","22")
    # return redirect("http://www.qq.com")
    # return response
    return render_template("user.html", name="flask demo", current_time=datetime.utcnow())
    # return render_template("user")
    # return "<p> your browser is: {0}</p>".format(user_agent)

@app.route("/form_demo", methods=["GET","POST"])
def form_demo():
    # name = None
    form = FormDemo()
    if form.validate_on_submit():
        session['name'] = form.name.data
        # name = form.name.data
        return redirect(url_for("form_demo"))
        # form.name.data = ''
    return render_template("form_demo.html", form=form, name=session.get('name'))

@app.route("/form_flash", methods=["GET","POST"])
def form_flash():
    form = FormDemo()
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash("look like you have changed name")
        session["name"] = form.name.data
        return redirect(url_for("form_flash"))
    return render_template("form_demo.html",form=form,name=session.get("name"))

@app.route("/form_db", methods=["GET","POST"])
def form_db():
    form = FormDemo()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session["known"] = False
        else:
            session["known"] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for("form_db"))
    return render_template("form_demo.html",form=form,name=session.get("name"),known=session.get("known", False))

@app.route("/form_mail", methods=["GET","POST"])
def form_mail():
    form = FormDemo()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data)


