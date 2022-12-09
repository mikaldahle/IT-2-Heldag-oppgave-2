import csv
import matplotlib.pyplot as plt
import numpy as np
class befolkning:
    def __init__(self, filnavn):
        self.filnavn = filnavn
    def åpne(self):
        with open(self.filnavn, encoding="utf-8-sig") as fil:
                self.filinnhold = list(csv.reader(fil, delimiter=";"))
                self.årstall, self.ekteskap, self.skilsmisser = self.filinnhold[2], self.filinnhold[3], self.filinnhold[4] #Filinhold i lister med overskrift og data
                self.x = self.årstall[1:] #data uten overskrift
                y = self.ekteskap[1:]
                z = self.skilsmisser[1:]
                self.dataY= []
                for a in y: #Gjør string om til int
                    if a.isnumeric() == True:
                        self.dataY.append(int(a))
                    else:
                        self.dataY.append(0)
                self.dataZ = []
                for b in z: #Gjør string om til int, og gjør ".." om til 0
                    if b.isnumeric() == True:
                        self.dataZ.append(int(b))
                    else:
                        self.dataZ.append(0)
                print(self.årstall, self.ekteskap, self.skilsmisser)
    def plot(self):
        X_akse = np.arange(len(self.x))
        plt.bar(X_akse - 0.2, self.dataY, 0.4, label = self.ekteskap[0])
        plt.bar(X_akse + 0.2, self.dataZ, 0.4, label = self.skilsmisser[0])
                
        plt.xticks(X_akse, self.x)
        plt.xlabel(self.årstall[0])
        plt.ylabel("Antall")
        plt.title("Skilsmisser og ekteskap")
        plt.legend()
        plt.show()
fil =befolkning("Skilsmisser og ekteskap.csv")
fil.åpne()
fil.plot()
