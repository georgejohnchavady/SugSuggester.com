import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Libraries for lemmatization
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer 
from nltk.stem import LancasterStemmer

def main():
    testTrainData=pd.read_csv("test.csv")
    scraped_Data_Comment=testTrainData['Comment Keywords']
    scraped_Data_Submissions=testTrainData['Submission Keywords']
    
    finalData_X=testTrainData.drop(['Subreddits commented in'],axis=1)
    finalData_Y=testTrainData['Subreddits commented in']
    
    
                        #****scraping comments****    
    flat_list_comments = []    
    #converting string to list
    flat_list_comments=splitCellString(scraped_Data_Comment,flat_list_comments)            
    #converting list[list] into list[]
    Comment_Keywords=removNestings(flat_list_comments)
    print(len(Comment_Keywords))    
    #getting unique list of keyword for features
    print(len(getUniqueKeywords(Comment_Keywords)))    
    unique_Comment_Keywords=getUniqueKeywords(Comment_Keywords)    
    finalData_X=createFeatures(finalData_X,unique_Comment_Keywords)       
    print(finalData_X.columns.tolist())    
    finalData_X.to_csv("output.csv",index=False)
    
                        #****scraping submissions****    
    flat_list_submissions = []    
    #converting string to list
    flat_list_submissions=splitCellString(scraped_Data_Submissions,flat_list_submissions)            
    #converting list[list] into list[]
    Submissions_Keywords=removNestings(flat_list_submissions)
    print(len(Submissions_Keywords))    
    #getting unique list of keyword for features
    print(len(getUniqueKeywords(Submissions_Keywords)))    
    unique_Submissions_Keywords=getUniqueKeywords(Submissions_Keywords)    
    finalData_X=createFeatures(finalData_X,unique_Submissions_Keywords)       
    print(finalData_X.columns.tolist())   
    print(len(finalData_X.columns.tolist()))
#    print(len(getUniqueKeywords(finalData_X.columns.tolist())))    

                        #****Adding feature occurences**** see below            
        
#    finalData_X.to_csv("output.csv",index=False)   
                        
    insertFeatureValues(finalData_X)
    print(finalData_X.head)
    finalData_X.to_csv("output.csv",index=False)   
    
    

def getUniqueKeywords(Keywords):
    stemmed_Keywords=[]
    tokenized_Keywords=[]
    tokenized_Keywords=tokenizeKeywords(Keywords)
    stemmed_Keywords=stemKeywords(tokenized_Keywords)
    
    unique_Keywords=[]
    for x in stemmed_Keywords:
        if x not in unique_Keywords:
            unique_Keywords.append(x)
    
    return unique_Keywords

def tokenizeKeywords(Keywords):
    token_words=[]
    for keyword in Keywords:
#        token_words.append(word_tokenize(keyword))
        print(type(word_tokenize(keyword)))
        print(word_tokenize(keyword))
        
    token_words=removNestings(token_words)
    return token_words


def stemKeywords(Keywords):  
    stemmed_Keywords = []   
    porter = PorterStemmer()
    lancaster=LancasterStemmer()
    for keyword in Keywords:
        stemmed_Keywords.append(str(lancaster.stem(keyword)))

    return stemmed_Keywords  
             
    
def removNestings(flat_list): 
    output=[]
    for x in flat_list:
        for y in x:
            output.append(y)
    return output

def createFeatures(finalData_X,unique_Comment_Keywords):
    for x in unique_Comment_Keywords:
        if x not in finalData_X.columns.tolist():
            if(x is not ""): #check for NaN values
                finalData_X[x]=0
    return finalData_X
        
def splitCellString(scraped_Data,flat_list):
    for sublist in scraped_Data:
        output = sublist.split(',')
        flat_list.append(output)
    return flat_list

def insertFeatureValues(finalData_X):
    row_count=int(finalData_X.shape[0]) #returns  length-1
    col_count=len(finalData_X.columns.tolist()) #returns exact length
    for i in range(5,col_count-1):
        for j in range(1,3):
            for k in range(0,row_count):
                
                if(finalData_X.iloc[k,j].find(finalData_X.columns[i])!=-1):
                    count=finalData_X.iloc[k,j].count(finalData_X.columns[i])
                    finalData_X.iloc[k,i]=count
                    
                
        
    
    
    
    
    
#    for i in range (4,10):
#        print(type(flat_list))
#        print(flat_list[i])
    
if __name__=="__main__":
        main() 