# -*- coding: utf-8 -*-

# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) October 12, 2015


##########################################################################
## Imports
##########################################################################

from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split as tts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics

import numpy as np
import pickle

##########################################################################
## Constants
##########################################################################

random_language_id = [10, 7, 3, 2, 11, 7, 4, 2, 12, 5, 6, 8, 0, 9, 1]

random_test = ['самая большая страна в мире','campanili e cupole contro il verde intenso delle', 
                    'vérifiez auparavant que le sujet', 'this is a test', 'solo una prueba', 
                    'porzione più bassa della tastiera la seconda per quella più alta', 'nein', 'hello world',
                    'ข้าพเจ้าทำหนังสือเดินทางหาย ข้าพเจ้าควรทำอย่างไร', 'οὖν καὶ τὴν ἄλλην πόλιν καὶ περισκοπῶν τὰ ἀναθήματα, ὁρῶ',
                    'पूरा कर दिया था उसी पर उसने स्वयं ही नशतर रख दिया', 'ハロウィーンナゼ日本でブレイク', 'ওঠা এক শোকের মিছিল। মিছিলের',
                    'arrancou para um início de época prometedor', 'te zorgen dat de advertenties worden aangepast aan']
    
##########################################################################
## Program
##########################################################################

if __name__ == "__main__":

    corpus = load_files("LanguageFolder")
 
    X_train, X_test, y_train, y_test = tts(corpus.data, corpus.target, test_size=0.20)
        
    text_clf = Pipeline([
        ('vec', CountVectorizer(analyzer='char_wb')),
        ('clf', MultinomialNB())
    ])
        
    text_clf = text_clf.fit(X_train, y_train)
    
    #Store the instance using pickle.
    with open('experiment_file_4','w') as f:
        pickle.dump(text_clf,f)
    
    #Predict language for test data.
    predicted = text_clf.predict(X_test)
    
    #Check model performance on test data.    
    accuracy = np.mean(predicted==y_test)
    print "Accuracy with test data: ", accuracy  
    
    #Use metrics module to further evaluate model performance.
    print(metrics.classification_report(y_test, predicted, 
        target_names = corpus.target_names))
  
    #Predict language for random snippets.
    predicted_random = text_clf.predict(random_test)
    
    #Check model performance for some random snippets. 
    random = np.array(random_language_id)
    accuracy_random = np.mean(predicted_random==random)  
    print predicted_random
    print "Accuracy of random snippets: ", accuracy_random
      
     
    
    