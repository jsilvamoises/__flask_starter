# -*- coding: utf-8 -*-
from app import app

if __name__ == "__main__":
    app.debug=True    
    app.run(host='0.0.0.0',port=80)

