#IMPORTING NECESSARY LIBRARIES
from src.logger import logging
from src.exception import CustomException

class ValidateString:
    logging.info("Program Started")
    def equivalence(self,string):
        try:
            logging.info(f"String to Check is : {string}")
            sent=string.replace(" ","").lower() #REPLACING SPACES WITH BLANK AND LOWERING CHARACTERS
            sentd = {w: 0 for w in sent} #CREATING DICTIONARY TO STORE DISTINCT CHARACTERS
            for char in sent:
                sentd[char]+=1
            print(sentd)
            logging.info(f"Count of Alphabets : {sentd}")
            first_key=next(iter(sentd)) # Count of previous value of key
            ctp = sentd[first_key]
            ctc=0 #Count of Current value
            ct=0 #Count Function
            for i in sentd.values(): # COMPARING VALUES OF KEYS AND KEEPING A RECORD OF DIFFERENCE OF VALUES
                ctc=i
                if ctc-ctp!=0:
                    ct+=1
                ctp=ctc
            if ct>1: # IF COUNT GREATER THAN 1 THEN RETURN NO ELSE RETURN YES
                return "NO!"
                logging.info("String not Valid")
            logging.info("String Valid")
            return "Yes!"
            
        except Exception as e: #HANDLING ERRORS IF OCCURS
            logging.info("Exception Occured while validating String")
            raise CustomException(e,sys)


if __name__ =="__main__":
    String1="AABBCCARSTW"
    String2="SSOONNIII"
    OBJ=ValidateString()
    A1=OBJ.equivalence(String1)
    A2=OBJ.equivalence(String2)
    print(String1,A1)
    print(String2,A2)


    """
    OUTPUT:
        {'a': 3, 'b': 2, 'c': 2, 'r': 1, 's': 1, 't': 1, 'w': 1}
        {'s': 2, 'o': 2, 'n': 2, 'i': 3}
        AABBCCARSTW NO!
        SSOONNIII Yes!
    """