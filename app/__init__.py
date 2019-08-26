# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 19:39:43 2019

@author: Usuario
pip freeze > requirements.txt
"""

from flask import Flask

app = Flask(__name__)


from app.controllers import default