from main import index
import os.path
import random
import math
import numpy as np

alpha = ['a', 'b', 'c', 'd', 'e', 'f']


def unweighted(query_unweight):
    dictionary= {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0}
    query_unweight=query_unweight.strip()
    for i in query_unweight:
        if i == " ":
            continue
        dictionary[i]+=1
    maxi= dictionary.values()
    maxi= max(maxi)
    for i in dictionary:
        dictionary[i]=dictionary[i]/maxi
    idf=calc_log()
    for i in dictionary:
        dictionary[i]=idf[i]*dictionary[i]
    return dictionary
    



def writenumber(query):
    query = query.strip()
    query = query[1:-1]
    query = query.split(";")
    query = {p.split(":")[0]: p.split(":")[1]for p in query}
    dictionary = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0}
    for i in query:
        dictionary[i] = float(query[i])
    return(dictionary)
#query= writenumber("<a:0.3;b:0.6;c:0.8;f:0.1>")


def CreateFiles():
    save_path = 'C:\\Users\\Mohamed hesham\\Desktop\\IR_Project'
    file_name = "text"
    n = 0
    
    while n <= 9:
        char = random.randint(5,10) 
        completeName = os.path.join(save_path, file_name+str(n)+".txt")

        file1 = open(completeName, "w")
        n += 1
        i = 1
        x = " "
        while(i < char):
            x += random.choice(alpha)
            x += " "
            i += 1
        file1.write(x)


def calc_freq():
    save_path = 'C:\\Users\\Mohamed hesham\\Desktop\\IR_Project'
    file_name = "text"
    
    n = 0
    freq_list = []

    while n <= 9:
        completeName = os.path.join(save_path, file_name+str(n)+".txt")

        freq = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
        file2 = open(completeName, "r")
        string = file2.read()
        string = string.strip()
        num_char = (len(string)+1)//2
        
        string = string.lower()
        n += 1
        for char in string:
            if (char == ' '):
                continue
            freq[char] += 1
        for key in freq:
            
            freq[key] /= num_char
        #print(num_char)    
            
        freq_list.append(freq)
    #print(freq_list)
        
    return freq_list


def calc_tfi():
    save_path = 'C:\\Users\\Mohamed hesham\\Desktop\\IR_Project'
    file_name = "text"
    num_char = 500
    n = 0
    tfi = []
    while n <= 9:
        completeName = os.path.join(save_path, file_name+str(n)+".txt")

        freq = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
        file2 = open(completeName, "r")
        string = file2.read()
        string=string.lower()
        n += 1
        for char in string:
            if (char == ' '):
                continue
            freq[char] += 1
        Num_list = [*freq.values()]
        Max_Value = max(Num_list)

        for key in freq:
            freq[key] /= Max_Value
        tfi.append(freq)

    print(tfi)
    return tfi


def calc_df():
    x = calc_freq()
    df = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
    for dictionary in x:
        for char in dictionary:
            if(dictionary[char] > 0):
                df[char] += 1

    return df


def Statistical_Model(query):
    
    x = calc_freq()
    C = []
    index=[0,1,2,3,4,5,6,7,8,9]

    for dictionary in x:
        d = {}
        for key, val in dictionary.items():
            d.update({key: dictionary[key] * query[key]})


        C.append(d)
    
    model1=[]
    for i in C:
        model1.append(sum(i.values()))
    list_tuples2= list(zip(model1,index))
    list_tuples2.sort(key=lambda x:x[0],reverse=True)

    return listofTuples(list_tuples2)

def calc_log():
    y = calc_df()
    df = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
    N = 10
    log = []
    for i in y:
        df[i] = math.log2((N/y[i]))
    return df


def calc_Idfi():
    tf = calc_tfi()
    df = calc_log()
    TF = []
    for l in tf:
        tf = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
        for key in l:
            tf[key] = l[key]*df[key]
        TF.append(tf)
    return (TF)


def calc_cosine(query):
    x = calc_Idfi()
    C = []
    index=[0,1,2,3,4,5,6,7,8,9]
    count=0
    for l in x:
        cosine = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
        for key in l:
            cosine[key] = l[key]*query[key]
        demonitor=sum(cosine.values())
        sq1=sum(np.square(np.array(list(l.values()))))
        sq2=sum(np.square(np.array(list(query.values()))))
        if((sq1*sq2)==0):
            C.append(0)
        else:
            C.append(demonitor/math.sqrt(sq1*sq2))
    lst_tuple = list(zip(C,index))
    lst_tuple.sort(key=lambda x:x[0],reverse=True)
       

    
    return listofTuples(lst_tuple)
def listofTuples(x):
    str1 =""
    for i in x:
        str1+="document "+str(i[1])+"      value"+str(i[0])+"<br>"
    return str1 
    

def listToString(s):     
    str1 = " " 
    for i in s:
        str1+=str(i)+"<br> "
    return (str1)
#calc_cosine(query)
#print(Statistical_Model(query))
calc_freq()
# calc_cosine()

