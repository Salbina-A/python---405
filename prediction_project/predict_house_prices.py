import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from math import sqrt
import pymongo
import os.path



if os.path.isfile('houses_train.csv'):
    houses = pd.read_csv('houses_train.csv')
    houses.head()
    
else:    
    raise NameError("File not found!")

if (houses.isnull().sum()).sum() == 0:
    reg = LinearRegression()
else:
    raise ValueError("Input contains NaN, infinity or a value too large for dtype")


class DataConv():
    def __init__(self, data):
        self.data = data

    def cond_conv(self):
        conv_cond = [2 if value == "good" else 1 if value == "newly repaired" else 0 for value in self.data.condition]
        self.data["condition"] = conv_cond

    def distr_conv(self):        
        conv_dist = [10 if value == "Achapnyak" else 9 if value == "Malatia-Sebastia" else 8 if value == "Shengavit"
        else 7 if value == "Davtashen" else 6 if value == "Arabkir" else 5 if value == "Center" else 4 if value == "Erebuni"
        else 3 if value == "Qanaqer-Zeytun" else 2 if value == "Nor Norq" else 1 if value == "Avan" else 0 for value in self.data.district
        ]
        self.data["district"] = conv_dist

    def buildingt_conv(self):
        conv_building_type = [2 if value == "stone" else 1 if value == "monolit" else 0 for value in self.data.building_type]
        self.data["building_type"] = conv_building_type

    def data_for_train(self):
        self.cond_conv()
        self.distr_conv()
        self.buildingt_conv()
        

    def split_train_test(self, validation_size = 0.2):
        label = self.data["price"] 
        self.data_preprocessing()               

        df_x = pd.DataFrame(self.data)
        df_y = pd.DataFrame(label)

        return train_test_split(df_x , df_y , test_size = validation_size, random_state = 30)


    def data_preprocessing(self):
        self.data = self.data.drop(["Unnamed: 0", "price", "url", "region", "street"], axis = 1)
        self.data_for_train()
        


class Regression_Model():    
    def __init__(self, data):
        self.converter = DataConv(data)    

    def train(self):
        self.x_train , self.x_test , self.y_train , self.y_test = self.converter.split_train_test()        
        reg.fit(self.x_train,self.y_train)        
        
        #print(reg.score(self.x_test,self.y_test))
        #print(reg.coef_)

        self.y_pred = reg.predict(self.x_test)
        self.mean_errors()
        print(self.y_pred)
        

    def mean_errors(self): 
        print((np.mean(self.y_pred - self.y_test)**2))
        print(mean_squared_error(self.y_test, self.y_pred))
        print(sqrt(mean_squared_error(self.y_test, self.y_pred)))


    def show_plot(self):
        y_plot = plt.plot(self.x_test, self.y_pred, 'b-')
        plt.show()


t = Regression_Model(houses)
t.train()
t.show_plot()
