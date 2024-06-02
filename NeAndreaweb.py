from flask import Flask, render_template

from html import *


web_app = Flask(__name__)

@web_app.route('/')#can add home to get home page other wise it will just take you strate to page
def home_page():
  
 return render_template('/index.html')#becouse we put this in the indext it will led us to the index page, we will call it home
list_of_Acomplishments_post = [
{"Title":"Project","Creater":"date"},
{"Title":"Innavator","NeAndrea":"4-24-24"}
]

@web_app.route('/Acomplishments')
def Acomplishments():
    
        return render_template('Acomplishments.html',data=list_of_Acomplishments_post)

@web_app.route('/Portfolio')
def Portfolio():
    return render_template('Portfolio.html')

@web_app.route('/Objectives')
def Objectives():
    return render_template('Objectives.html')


@web_app.route('/SIP')
def SIP():
    return render_template('SIP.html')

if __name__ == '__main__':
    web_app.run(debug=True)# we set this so we can see the editds in real time once we refresh the page.