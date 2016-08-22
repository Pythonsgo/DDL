

from flask import Flask, render_template, request, redirect

import pickle
import numpy as np


##########################################################################
## Constants
##########################################################################
Language_list = ['Bengali', 'Dutch', 'English', 'French', 'German', 'Greek',
                 'Hindi', 'Italian', 'Japanese', 'Portuguese', 'Russian', 'Spanish', 'Thai']

text_clf = pickle.load(open('trained_model','r'))
##########################################################################
## Modules
##########################################################################

app = Flask(__name__)

#Variable to hold the text input from user for language Identification.
TEXT=''       

#Module which obtains user input.
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('info.html')
    else:
        TEXT = request.form['user_info']
    
        text_string = [TEXT]
    
        predict_string = text_clf.predict(text_string)
    
        LANGUAGE = Language_list[predict_string]
                        
        #Go to  prediction.html template for display of language in which text is written.
        return render_template('prediction.html', language=LANGUAGE)

#Module redirects the user back to the input page for a new language identification request.
@app.route('/next')
def next():
    return redirect('/index') 

##########################################################################
## Program 
##########################################################################
    
if __name__ == "__main__":
    app.run()
    
