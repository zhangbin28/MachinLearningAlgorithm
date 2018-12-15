# Candidate-Elimination algorithm
# book:Machine learning, Tom-Mitchell, chapter 8, P232
# zhang bin, 2018/12/13
# 

import dataset as ds

class KNN(object):
    def __init__(self, train_set, values, dest_key, k):
        self.train_set = train_set
        self.values = values
        self.dest_key = dest_key
        self.param_k = k


    def train(self):
        return

    def test(self, data):
        distence = []
        for item in self.train_set:
            distence.append({'dis':self.CalcDistence(data, item), 'label':item[self.dest_key]})

        distence.sort(key = lambda x:x['dis'])

        count = 0
        for idx in range(0, self.param_k):
            if distence[idx]['label']=='Yes':
                count+= 1 if distence[idx]['dis']==0 else 1/(distence[idx]['dis']**2)
            else:
                count-= 1 if distence[idx]['dis']==0 else 1/(distence[idx]['dis']**2)

        return count > 0


    def CalcDistence(self, a, b):
        sum = 0
        for key in a:
            if a[key] != b[key]:
                sum += 1
        
        return sum
        

def getTrainData():
    return [{'Sky':'Sunny', 'AirTemp':'Warm', 'Humidity':'Normal', 'Wind':'Strong', 'Water':'Warm', 'Forecast':'Same','EnjoySport':'Yes'}, \
            {'Sky':'Sunny', 'AirTemp':'Warm', 'Humidity':'High', 'Wind':'Strong', 'Water':'Warm', 'Forecast':'Same','EnjoySport':'Yes'}, \
            {'Sky':'Rainy', 'AirTemp':'Cold', 'Humidity':'High', 'Wind':'Strong', 'Water':'Warm', 'Forecast':'Change','EnjoySport':'No'}, \
            {'Sky':'Sunny', 'AirTemp':'Warm', 'Humidity':'High', 'Wind':'Strong', 'Water':'Cool', 'Forecast':'Change','EnjoySport':'Yes'}]
values = {'Sky':['Sunny','Rainy','Cloudy'], \
        'AirTemp':['Cold','Warm'], \
        'Humidity':['Normal','High'], \
        'Wind':['Weak','Strong'], \
        'Water':['Warm','Cold'], \
        'Forecast':['Same','Change']}

f = KNN(ds.getTrainData(), ds.values, 'EnjoySport',3)

f.train()

#f.PrintTrainResult()

print(f.test({'Sky':'Sunny', 'AirTemp':'Warm', 'Humidity':'Normal', 'Wind':'Strong', 'Water':'Cool', 'Forecast':'Change'}))
print(f.test({'Sky':'Rain', 'AirTemp':'Cold', 'Humidity':'Normal', 'Wind':'Light', 'Water':'Warm', 'Forecast':'Same'}))
print(f.test({'Sky':'Sunny', 'AirTemp':'Warm', 'Humidity':'Normal', 'Wind':'Light', 'Water':'Warm', 'Forecast':'Same'}))
print(f.test({'Sky':'Rainy', 'AirTemp':'Cold', 'Humidity':'High', 'Wind':'Strong', 'Water':'Warm', 'Forecast':'Change'}))
