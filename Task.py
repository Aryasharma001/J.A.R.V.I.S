import datetime 
from speak import Say 
import pywhatkit
import wikipedia 

def Time():
    time=datetime.datetime.now().strftime("%H:%M")
    Say(time)
    
def Date():
    date=datetime.date.today()
    Say(date)
    
def Day():
    day=datetime.datetime.now().strftime("%A")
    Say(day)
        
    
    
def non_input_execution(query):
    query=str(query)
    
    if "time" in query:
        Time() 
        
    elif "date" in query:
        Date()   
        
    elif "day" in query:
        Day()         
      
      

    
def input_execution(tag,query):
    
    if query:
        result = wikipedia.summary(query)
        print(result)
    else:
        print("Invalid input")
        
        
    if "google" in tag:
        name=str(query).replace("google","")
        query=query.replace("search"," ") 
        pywhatkit.search(query)