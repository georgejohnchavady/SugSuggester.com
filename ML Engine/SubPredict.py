import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def main():
    testTrainData=pd.read_csv("test.csv")
       
    scraped_Data_Features=testTrainData['Comment Keywords']
    flat_list = []
    
    #converting string to list
    for sublist in scraped_Data_Features:
        output = sublist.split(',')
        flat_list.append(output)
            
    #converting list[list] into list[]
    Comment_Keywords=removNestings(flat_list)
    print(len(Comment_Keywords))
    
    #getting unique list of keyword for features
    print(len(getUniqueKeywords(Comment_Keywords)))
    
            


def getUniqueKeywords(Comment_Keywords):
    unique_Comment_Keywords = []
    for x in Comment_Keywords:
        if x not in unique_Comment_Keywords:
            unique_Comment_Keywords.append(x)
    return unique_Comment_Keywords
        
    
             
    
def removNestings(flat_list): 
    output=[]
    for x in flat_list:
        for y in x:
            output.append(y)
    return output

def createFeatures():
    
    
#    for i in range (4,10):
#        print(type(flat_list))
#        print(flat_list[i])

    
    
    
    
    
if __name__=="__main__":
    main()