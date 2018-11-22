# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 11:04:09 2018

@author: suryaprakash.rao
"""

from flask import Flask,request
#from flask import make_response
#from flask import jsonify
from flask_json import FlaskJSON, as_json_p
from Chattertest import bot1

app = Flask(__name__)
json = FlaskJSON(app)
app.config['JSON_ADD_STATUS'] = False
app.config['JSON_JSONP_OPTIONAL'] = False

print (app.app_context())
with app.app_context():
    ctx=app.app_context()
    ctx.push()
    
    @app.route("/")
    def home():
        return ("hi")
    @app.route("/index")
    
    @app.route('/login', methods=['GET', 'POST'])
    @as_json_p
    def login():
        qus=request.args.get('mydata')    
        ans=bot1(str(qus))
        test="Bot :" + "="+ str(ans)
        return (test) 

    if __name__ == "__main__":
        app.run(debug = True)