# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:26:07 2018

@author: Pradipta
"""
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from math import sqrt
from collections import Counter
style.use('fivethirtyeight')

#plot1 = [1,3]
#plot2 = [2,5]
#euclidean_distance = sqrt( (plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2 )
#print(euclidean_distance)


def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups!')
        
    distances = []
    for group in data:
        for features in data[group]:
            #euclidean_distance = sqrt( (features[0]-predict[0])**2 + (features[1]-predict[1])**2 )
            ##euclidean_distance = np.sqrt(np.sum((np.array(features)-np.array(predict))**2))
           ## print(euclidean_distance)
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            print(euclidean_distance,group)
            distances.append([euclidean_distance,group])
    votes = [i[1] for i in sorted(distances)[:k]]
    #print(Counter(votes).most_common(2))
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [5,7]
result = k_nearest_neighbors(dataset, new_features,k=5)
print(result)
[[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1] , color = result)  
plt.show()