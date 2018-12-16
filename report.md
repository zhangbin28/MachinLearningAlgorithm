# 机器学习报告

## 候选-消除算法
### 数据集

#### 训练集
Sky | AirTemp | Humidity | Wind | Water | Forecast | EnjoytSport 
| :-: | :-: | :-: |:-: |:-: |:-: | :-: | 
Sunny | Warm | Normal | Strong | Warm | Same | Yes 
Sunny | Warm | High | Strong | Warm | Same | Yes 
Rainy | Cold | High | Strong | Warm | Change | No
Sunny | Warm | High | Strong | Cold | Change | Yes

#### 待分类数据
Sky | AirTemp | Humidity | Wind | Water | Forecast
| :-: | :-: | :-: |:-: |:-: |:-: | :-: | 
Sunny | Warm | Normal | Strong | Cold | Change 
Rainy | Cold | Normal | Light | Warm | Same 
Sunny | Warm | Normal | Light | Warm | Same
Sunny | Cold | High | Strong | Warm | Change

### 算法流程
- 将G集合初始化为H中极大一般假设
- 将S集合初始化为H中极大特殊假设
- 对每个训练样例d，进行以下操作
    - 如果d是一正例
        - 从G中移去所有与d不一致的假设
        - 对S中每个与d不一致的假设s
            - 从S中移去s
            - 把s的所有的极小泛化式h加入到S中，其中h满足
                - h与d一致，而且G的某个成员比h更一般
            - 从S中移去所有这样的假设：它比S中另一假设更一般
    - 如果d是一个反例
        - 从S中移去所有与d不一致的假设
        - 对G中每个与d不一致的假设g
            - 从G中移去g
            - 把g的所有的极小特化式h加入到G中，其中h满足
                - h与d一致，而且S的某个成员比h更特殊
            - 从G中移去所有这样的假设：它比G中另一假设更特殊

### 算法实现
'''' cpp
    int a;
''''

### 结果

### 分析评价

header 1 | header 2
---|---
row 1 col 1 | row 1 col 2
row 2 col 1 | row 2 col 2


Sky | AirTemp | Humidity | header 2 | header 2 | header 2
---|---|---|---|---|---
Sky | AirTemp | Humidity | Wind|Water | Forecast | EnjoytSport 
Sky | AirTemp | Humidity | Wind|Water | Forecast | EnjoytSport 
