# Nicolai og Mikal 09.12.2022
#  
import matplotlib.pyplot as plt
import numpy as np
from classfilereader import *

con = main()

class subclass():
    def __init__(self, data):
        self.data = data.content
        self.headlines = data.headlines
        self.type = data.type
        self.x = []
        self.y = []

        if data.type == 'json':
            self.x = [i for i in self.data[0]['dataset']
                      ['dimension']['Tid']['category']['index']]
            self.y = [i for i in self.data[0]['dataset']['value']]


class mainclass():
    def __init__(self):
        self.data = [subclass(i) for i in con]


mclass = mainclass()

for ind in mclass.data:
    if ind.type != 'json':
        for v in ind.data:
             if all(i.isnumeric() for i in v):
                  for i, v1 in enumerate(v):
                    v1 = int(v1)
                    if (i-1) % 2 == 0:
                        ind.y.append(v1)
                    else:
                        ind.x.append(v1)
        plt.title(ind.headlines)
        plt.xlabel('År')
        plt.ylabel('Antall')
        plt.xticks(ind.x[::50])
        plt.plot(ind.x, ind.y, label='Folketall')
        plt.legend()
        plt.show()
    else:
        newlist = []
        start = 0
        for i,v in enumerate(ind.y):
            i = i+1
            if i%len(ind.x)==0 and i != 0:
                newlist.append([v for v in ind.y[start:i]])
                start = i
        
        for i2,v in enumerate(newlist):
            plt.title(ind.data[0]['dataset']['label'])
            plt.plot(ind.x, v,label = ind.data[0]['dataset']['dimension']['EkteskStatus']['category']['label'][str(i2+1)])
            plt.xlabel('År')
            plt.ylabel('Antall')
            plt.xticks(ind.x[::5])
            plt.legend()
            plt.show()

        for i2,v in enumerate(newlist):
            plt.title(ind.data[0]['dataset']['label'])
            plt.plot(ind.x, v,label = ind.data[0]['dataset']['dimension']['EkteskStatus']['category']['label'][str(i2+1)])
            plt.xlabel('År')
            plt.ylabel('Antall')
            plt.xticks(ind.x[::5])
            plt.legend()
        plt.show()

highest = 0

for ind in mclass.data:
    if ind.type != 'json':
        plt.plot(np.linspace(0,highest,len(ind.y)),ind.y, label='Folketall')
        plt.legend()
    else:
        highest = int(len(ind.x))
        newlist = []
        start = 0
        for i,v in enumerate(ind.y):
            i = i+1
            if i%len(ind.x)==0 and i != 0:
                newlist.append([v for v in ind.y[start:i]])
                start = i
        
        for i2,v in enumerate(newlist):
            plt.plot(ind.x, v,label = ind.data[0]['dataset']['dimension']['EkteskStatus']['category']['label'][str(i2+1)])
            plt.xticks(ind.x[::5])
            plt.legend()

plt.xlabel('År')
plt.ylabel('Antall')
plt.title('Kombinert')
plt.show()
