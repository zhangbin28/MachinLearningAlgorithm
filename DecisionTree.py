# Candidate-Elimination algorithm
# book:Machine learning, Tom-Mitchell, chapter 3, P56
# zhang bin, 2018/12/15
# 

import math
import dataset as ds

class ID3(object):

    def __init__(self, data, values, dest_key):
        self.train_set = data
        self.values = values
        self.dest_key = dest_key



    def train(self):
        self.root = self.ID3(self.train_set, self.values)

    def ID3(self, data, set_values):
        node = {'leaf':False}

        count = 0
        for d in data:
            if d[self.dest_key] == 'Yes':
                count += 1
        
        if count == 0:
            node['leaf'] = True
            node['label'] = False
        elif count == len(data):
            node['leaf'] = True
            node['label'] = True
        
        if len(set_values) == 0:
            node['leaf'] = True
            if count > len(data) / 2:
                node['label'] = True
            else:
                node['label'] = False
        
        if node['leaf'] == False:
            maxValue = ''
            maxValue_v = 0

            for v in set_values:
                vv = self.CalcExamples(data, v, set_values[v])
                if vv > maxValue_v:
                    maxValue_v = vv
                    maxValue = v
            node['dec_v'] = maxValue
            node['childs'] = {}
            data_v = {}
            for v in set_values[maxValue]:
                data_v[v] = []
            for d in data:
                data_v[d[maxValue]].append(d)
            for v in set_values[maxValue]:
                if len(data_v[v]) == 0:
                    if count > len(data) / 2:
                        node['childs'][v] = {'leaf':True, 'label':True}
                    else:
                        node['childs'][v] = {'leaf':True, 'label':False}
                else:
                    t_set_values = set_values.copy()
                    del t_set_values[maxValue]
                    node['childs'][v] = self.ID3(data_v[v], t_set_values)
        
        return node




    def CalcExamples(self, data, key, values):
        v_count = {}
        count = {'Yes':0, 'No':0}
        for v in values:
            v_count[v] = {'Yes':0, 'No':0}
        for d in data:
            v_count[d[key]][d[self.dest_key]] += 1
            count[d[self.dest_key]] += 1

        total_num = count['Yes']+count['No']
        gain = 0
        if count['Yes']!=0 and count['No']!=0:
            gain = - count['Yes']/total_num * math.log(count['Yes']/total_num, 2)\
                - count['No']/total_num * math.log(count['No']/total_num, 2)
        
        for v in values:
            if v_count[v]['Yes']!=0 and v_count[v]['No']!=0:
                num = v_count[v]['Yes']+v_count[v]['No']
                gain -= num / total_num\
                    *(- v_count[v]['Yes']/num * math.log(v_count[v]['Yes']/num, 2)\
                    - v_count[v]['No']/num * math.log(v_count[v]['No']/num, 2))
        
        return gain
        
    def test(self, data):
        node = self.root
        ret = False

        while True:
            if node['leaf']:
                ret = node['label']
                break
            else:
                node = node['childs'][data[node['dec_v']]]

        return ret



f = ID3(ds.getTrainData(), ds.values, 'EnjoySport')

f.train()

print(f.test({'Sky':'Sunny', 'AirTemp':'Warm', 'Humidity':'Normal', 'Wind':'Strong', 'Water':'Cool', 'Forecast':'Change'}))
