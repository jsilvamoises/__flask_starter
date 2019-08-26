# -*- coding: utf-8 -*-
from app import app


@app.route("/")
def index():
    return '<h1>Hello world! <b>Jesus</b></h1>'

