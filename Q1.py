#IMPORTING LIBRARIES
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

class word_freq:
    def count(self,words):
        logging.info("Coutning has been Started")
        logging.info(f"The String is{words}")
        try:
            words=words.lower() #LOWERING WORDS
            word1=words.split(" ")#SPLITTING THE WORDS ND STORING IN DICTIONARY AND LIST TO TO COMPARE
            word = {w: 0 for w in words.split(" ")}
            for i in word1:
                if i in words:
                    word[i]+=1
            max_key = max(word, key=lambda k: word[k]) #FINDING KEY WITH MAX FREQ AND RETURNING ITS FREQUENCY AND LENGTH
            logging.info(f"Most frequent word and its length and count is {max_key} ,length is {len(max_key)},count is {max(word.values())}")
            return max(word.values()),max_key,len(max_key)
        except Exception as e:
            logging.info("Error Occured while Calculating in Count Function")
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    string="Apple Banana Apple Apple Banana Grapes Banana Banana Apple"
    string2="write write write all the numbers from from from 1 to 100"
    obj=word_freq()
    WF=obj.count(string)
    print(f"The most frequent word occured {WF[0]} times .The word is '{WF[1].upper()}' and its length is {WF[2]}")
    WF=obj.count(string2)
    print(f"The most frequent word occured {WF[0]} times .The word is '{WF[1].upper()}' and its length is {WF[2]}") 


'''
Output:
        The most frequent word occured 4 times .The word is 'APPLE' and its length is 5
        The most frequent word occured 3 times .The word is 'WRITE' and its length is 5
'''