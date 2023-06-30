import random 
from Task import non_input_execution
import json 
import torch 
from brain import NeuralNet
from NeuralNetwork import bag_of_words,tokenize 
from listen import Listen
from speak import Say
from Task import input_execution

device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json","r") as json_data:
    intents=json.load(json_data)
    
FILE="TrainData.pth"    
data=torch.load(FILE) 

input_size=data["input_size"]
hidden_size=data["hidden_size"]
output_size=data["output_size"]
all_words=data["all_words"]
tags=data["tags"]
model_state=data["model_state"]

model=NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#-------------------------
Name="Jarvis" 

def Main():
    sentence=Listen()
    result=str(sentence)
    
    if sentence =="bye" or sentence=="goodbye":
        exit() 
        
    sentence=tokenize(sentence) 
    X=bag_of_words(sentence,all_words)  
    X=X.reshape(1,X.shape[0])
    X=torch.from_numpy(X).to(device)
    
    output=model(X)
    
    _ ,predicted=torch.max(output,dim=1)
    tag=tags[predicted.item()]
    
    probs=torch.softmax(output,dim=1)
    
    prob=probs[0][predicted.item()]
    
    if prob.item()> 0.75:
        for intent in intents['intents']:
            if tag==intent["tag"]:
                reply=random.choice(intent["responses"])
                
                if "time" in reply:
                    non_input_execution(reply)
                
                elif "date" in reply:
                    non_input_execution(reply)
                    
                elif "day" in reply:
                    non_input_execution(reply)  
                    
                elif "wikipedia" in reply:
                    input_execution(reply,result)    
                    
                elif "google" in reply:
                    input_execution(reply,result)        
                else:    
                  Say(reply)

while True:
    Main()              