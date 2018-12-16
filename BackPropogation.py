# Candidate-Elimination algorithm
# book:Machine learning, Tom-Mitchell, chapter 4, P98
# zhang bin, UnDone
# 

import math
import dataset as ds
import random
import numpy as np


class BackPropogation(object):
    def __init__(self, data, values, dest_key, num_param_per_layer, num_layer):
        self.train_set = data
        self.values = values
        self.dest_key = dest_key

        self.num_param_per_layer = num_param_per_layer
        self.num_layer = num_layer

        self.eta = 0.5

        t_values = {}
        for v in self.values:
            t_values[v] = {}
            num = 0
            for vv in self.values[v]:
                t_values[v][vv] = num
                num += 1
        t_values[self.dest_key]={'Yes':1, 'No':0}

        self.num_input = len(data[0])-1
        self.num_out = 2

        self.train_label = []
        for d in data:
            dd = []
            for v in d:
                dv = t_values[v][d[v]]
                if v == self.dest_key:
                    self.train_label.append(np.array([0,1] if dv == 0 else [1,0]))
                else:
                    dd.append(dv)
            d = np.array(dd)
        self.t_values = t_values

        self.param = []
        for i in range(self.num_layer):
            matrix = []
            if i == 0:
                for j in range(self.num_input):
                    matrix.append(np.array(random.sample(range(-50, 50), self.num_param_per_layer)).astype('float32')/1000)    
            elif i == self.num_layer - 1:
                for j in range(self.num_param_per_layer):
                    matrix.append(np.array(random.sample(range(-50, 50), self.num_out)).astype('float32')/1000)
            else:
                for j in range(self.num_param_per_layer):
                    self.param.append(np.array(random.sample(range(-50, 50), self.num_param_per_layer)).astype('float32')/1000)
            self.param.append(np.array(matrix))

    def train(self, iteration):
        while iteration==0:
            for ii in range(len(self.train_set)):
                d = self.train_set[ii]
                d = (d- np.min(d))/(np.max(d)-np.min(d))
                ret_t = self.train_label[ii]

                ret = np.array(d)
                out = []
                for i in range(self.num_layer):
                    ret = np.dot(self.param[i], ret)
                    out.append(np.array(ret))

                error_k = np.dot(np.dot(ret, (1 - ret)), (ret_t - ret))

                error_k = [0] * self.num_out
                error_h = [[0] * max([self.num_param_per_layer, self.num_input, self.num_out])]*self.num_layer

                for i in range(self.num_out):
                    error_k[i] = ret[i]*(1-ret[i])*(ret_t[i]-ret[i])

                for i in range(self.num_layer-1, -1, -1):
                    if i == 0:
                        for j in range(self.num_input):
                            error_h[i][j] = ret[i][j] * (1 - ret[i][j])
                            sum = 0
                            for k in range(self.num_param_per_layer):
                                sum += self.param[i][j][k] * error_h[i+1][k]
                            error_h[i][j] *= sum

                    elif i == self.num_layer - 1:
                        for j in range(self.num_param_per_layer):
                            error_h[i][j] = ret[i][j] * (1 - ret[i][j])
                            sum = 0
                            for k in range(self.num_out):
                                sum += self.param[i][j][k] * error_k[k]
                            error_h[i][j] *= sum

                    else:
                        for j in range(self.num_param_per_layer):
                            error_h[i][j] = ret[i][j] * (1 - ret[i][j])
                            sum = 0
                            for k in range(self.num_param_per_layer):
                                sum += self.param[i][j][k] * error_h[i+1][k]
                            error_h[i][j] *= sum

                    for i in range(self.num_layer-1, -1, -1):
                        if i == 0:
                            for j in range(self.num_input):
                                for k in range(self.num_param_per_layer):
                                    self.param[i][j][k] += self.eta * error_h[i+1][k] * ret[i][j]

                        elif i == self.num_layer - 1:
                            for j in range(self.num_param_per_layer):
                                for k in range(self.num_out):
                                    self.param[i][j][k] += self.eta * error_h[i+1][k] * ret_t[j]

                        else:
                            for j in range(self.num_param_per_layer):
                                for k in range(self.num_param_per_layer):
                                    self.param[i][j][k] += self.eta * error_h[i+1][k] * ret[i][j]
            
            iteration -= 1

    def test(self, data):
        dd = []
        for v in data:
            dv = self.t_values[v][data[v]]
            dd.append(dv)
        d = np.array(dd)

        d = (d- np.min(d))/(np.max(d)-np.min(d))
        ret = np.array(d)
        for i in range(self.num_layer):
            ret = np.dot(self.param[i], ret)
        
        if np.linalg.norm((ret - [1,0]), 2) < np.linalg.norm((ret - [0,1]), 2):
            return True
        else:
            return False


f = BackPropogation(ds.getTrainData(), ds.values, 'EnjoySport', 5, 3)

f.train(10)

print(f.test({'Sky':'Sunny', 'AirTemp':'Warm', 'Humidity':'Normal', 'Wind':'Strong', 'Water':'Cold', 'Forecast':'Change'}))

        




                
                
                
                












    