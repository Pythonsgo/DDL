# -*- coding: utf-8 -*-

# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) October 12, 2015


##########################################################################
## Imports
##########################################################################

import pickle
import numpy as np


##########################################################################
## Constants
##########################################################################
Language_list = ['Bengali', 'Dutch', 'English', 'French', 'German', 'Greek',
                 'Hindi', 'Italian', 'Japanese', 'Portuguese', 'Russian', 'Spanish', 'Thai']


##########################################################################
## Program
##########################################################################

if __name__ == "__main__":
    
    #Load the model using pickle.
  
    text_clf = pickle.load(open('experiment_file_4','r'))
    
    
    #Request text from user to predict language.
    
    test_string = raw_input("Enter your sample text:")
    
    test_string= [test_string.decode('utf8')]
    
    predict_string = text_clf.predict(test_string)
    
    print "This text is written in:", Language_list[predict_string]
    

    

  
 
 
    
    
    
      
     
