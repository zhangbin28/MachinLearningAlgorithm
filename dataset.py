def getTrainData():
    return [{'Sky':'Sunny', 'AirTemp':'Warm', 'Humidity':'Normal', 'Wind':'Strong', 'Water':'Warm', 'Forecast':'Same','EnjoySport':'Yes'}, \
            {'Sky':'Sunny', 'AirTemp':'Warm', 'Humidity':'High', 'Wind':'Strong', 'Water':'Warm', 'Forecast':'Same','EnjoySport':'Yes'}, \
            {'Sky':'Rainy', 'AirTemp':'Cold', 'Humidity':'High', 'Wind':'Strong', 'Water':'Warm', 'Forecast':'Change','EnjoySport':'No'}, \
            {'Sky':'Sunny', 'AirTemp':'Warm', 'Humidity':'High', 'Wind':'Strong', 'Water':'Cold', 'Forecast':'Change','EnjoySport':'Yes'}]
values = {'Sky':['Sunny','Rainy','Cloudy'], \
        'AirTemp':['Cold','Warm'], \
        'Humidity':['Normal','High'], \
        'Wind':['Weak','Strong'], \
        'Water':['Warm','Cold'], \
        'Forecast':['Same','Change']}