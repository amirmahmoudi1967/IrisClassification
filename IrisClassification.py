# -*- coding: utf-8 -*-
"""
@author: Amir Mahmoudi
"""
import numpy as np

def k_nn(nbclasse,x):
    #creating the dataset
    places = []    
    with open('dataset.txt', 'r') as filehandle:
        places = [current_place.rstrip() for current_place in filehandle.readlines()]
    dataset=[]
    for i in range(len(places)):
        dataset.append(places[i].split(","))
    #creating the unkwon set in this set the class is missing and we will find it with the knn method
    places = []    
    with open('dataeval.txt', 'r') as filehandle:
        places = [current_place.rstrip() for current_place in filehandle.readlines()]
    unknown=[]
    for i in range(len(places)):
        unknown.append(places[i].split(",")) 
    
    classe=[]
    for i in range (nbclasse):  # number of class: 3 type of flower
        classe.append(0)
    k=x  # setting of k nn, k represents the number of neighbours we will check
    for i in range(len(unknown)):
        distance=[]
        classe=[0,0,0]
        for j in range (len(dataset)):
            distance.append((dataset[j][4],np.sqrt((float(unknown[i][0])-float(dataset[j][0]))**2 +(float(unknown[i][1])-float(dataset[j][1]))**2+(float(unknown[i][2])-float(dataset[j][2]))**2+(float(unknown[i][3])-float(dataset[j][3]))**2)))
        distance.sort(key=lambda distance:distance[1])
        #the list distance have the class of each element of the dataset and the distance of how far they are from each point of the unknown set
        for l in range(k):
            #filling the class list to determine the class of the unknown elements
            if distance [l][0]=="Iris-setosa":
                classe[0]+=1
            if distance [l][0]=="Iris-virginica":
                classe[1]+=1
            if distance [l][0]=="Iris-versicolor":
                classe[2]+=1
        temp=max(classe)
        #Affecting the class determined
        if(classe[0]==temp and classe[1]==temp) or (classe[1]==temp and classe[2]==temp) or (classe[0]==temp and classe[2]==temp):
            value=""
            if distance[0][0]=="Iris-setosa":
                value="Iris-setosa"
            elif distance[0][0]=="Iris-virginica":
                value="Iris-virginica"
            elif distance[0][0]=="Iris-versicolor":
                value="Iris-versicolor"
            unknown[i].append(value)
        else:
            a=(classe.index(max(classe)))+1
            value=""
            if a==1:
                value="Iris-setosa"
            elif a==2:
                value="Iris-virginica"
            elif a==3:
                value="Iris-versicolor"
            unknown[i].append(value)    
    print(unknown)     
            
k_nn(3,3)       
        
            
        
