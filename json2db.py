import requests
import json
import numpy as np

#Downloaded while migrating to show stuffs without internet
Batchlist  =['074','075','076','077']
Proglist  =['BCT', 'BEI', 'BEX', 'BEL']  #Limited for Demo
GroupList =['A','B','C','D']
def getStudentData(prog,batch,group):
    clause = {'prog':prog,'batch':batch,'group':group}
    r= requests.post('http://assmnt.pcampus.edu.np/api/students/',data=clause)
    data = json.loads(r.text)
    return data

def Data():
    StdList=[]
    SecList=[]
    for i in Proglist:
        for j in Batchlist:
            for k in GroupList:
                temp = getStudentData(i,j,k)
                if(len(temp) != 0):
                    for x in temp:
                        temp2 = [{ 
                            "model":"classes.StudentData",
                            "pk":len(StdList) +1,
                            "fields":{ 
                            "Batch": x[0], 
                            "Dept": x[1], 
                            "Roll": x[2],
                            "Section":k,
                            "Name": x[3]}}]
                        StdList =[*StdList,*temp2]
                    SecList =[*SecList,[j,i,k]]
                   
    
    # StdList = [{ 
    #     "model":"PortalApp.StudentData",
    #     "pk":StdList.index(x)+1,
    #     "fields":{ 
    #         "Batch": x[0], 
    #         "Dept": x[1], 
    #         "Roll": x[2],
    #         "Name": x[3]}} for x in StdList]
    
    SecList =[{
        "model":"classes.classData",
        "pk":SecList.index(x)+1 ,
        "fields":{ 
            "batch": x[0], 
            "dept": x[1], 
            "sec": x[2]}} for x in SecList]
    return json.dumps([*StdList,*SecList])


with open('Data.json', 'w') as file:
    file.write(Data())



