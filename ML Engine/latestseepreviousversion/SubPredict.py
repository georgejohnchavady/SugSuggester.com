import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def main():
    testTrainData=pd.read_csv("test.csv")
       
    scraped_Data_Comment=testTrainData['Comment Keywords']
    finalData=testTrainData
    flat_list_comments = []
    
    #converting string to list
    flat_list_comments=splitCellString(scraped_Data_Comment,flat_list_comments)
            
    #converting list[list] into list[]
    Comment_Keywords=removNestings(flat_list_comments)
    print(len(Comment_Keywords))
    
    #getting unique list of keyword for features
    print(len(getUniqueKeywords(Comment_Keywords)))    
    unique_Comment_Keywords=getUniqueKeywords(Comment_Keywords)
    
    finalData=createFeatures(finalData,unique_Comment_Keywords)    
    
    print(finalData.columns.tolist())
    
    finalData.to_csv("output.csv",index=False)

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

def createFeatures(finalData,unique_Comment_Keywords):
    for x in unique_Comment_Keywords:
        finalData[x]=0
    return finalData
        
def splitCellString(scraped_Data,flat_list):
    for sublist in scraped_Data:
        output = sublist.split(',')
        flat_list.append(output)
    return flat_list
    
    
#    for i in range (4,10):
#        print(type(flat_list))
#        print(flat_list[i])
    
if __name__=="__main__":
        main() 