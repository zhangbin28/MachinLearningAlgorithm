# Candidate-Elimination algorithm
# book:Machine learning, Tom-Mitchell, chapter 2, P33
# zhang bin, 2018/11/02
# 

import dataset as ds

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

class CandidateElimination(object):
    def __init__(self, data, values, dest_key):
        self.train_set = data
        self.values = values
        self.dest_key = dest_key
        self.version_sapce = []

        self.dS, self.dG = self.InitSpace()

    def InitSpace(self):
        ret_item_ds = {}
        ret_item_dg = {}
        
        for key in self.values:
            ret_item_ds[key] = '$'
            ret_item_dg[key] = '?'

        return [ret_item_ds], [ret_item_dg]

    def train(self):
        for d in self.train_set:
            if d[self.dest_key] == 'Yes':
                idx = 0
                while idx < len(self.dG):
                    if not self.isConsistent(self.dG[idx], d):
                        self.dG.pop(idx)
                        idx-=1
                    idx += 1

                idx = 0
                while idx < len(self.dS):
                    s = self.dS[idx]
                    if not self.isConsistent(s, d):
                        self.dS.pop(idx)
                        idx -= 1
                        
                        min_general = self.getMinih_general(s, d, self.dG)
                        for hh in min_general:
                            self.dS.append(hh)

                        self.checkGeneral(self.dS)
                    idx += 1
            else:
                idx = 0
                while idx < len(self.dS):
                    if self.isConsistent(self.dS[idx], d):
                        self.dS.pop(idx)
                        idx-=1
                    idx += 1

                idx = 0
                while idx < len(self.dG):
                    g = self.dG[idx]
                    if self.isConsistent(g, d):
                        self.dG.pop(idx)
                        idx-=1

                        min_specific = self.getMinih_specific(g, d, self.dS, self.values)
                        for hh in min_specific:
                            self.dG.append(hh)

                        self.checkGeneral(self.dG)
                    idx += 1
        self.GenVp()

    # 新的实例只在变形空间所有成员都进行同样分类时才输出分类结果，否则系统拒绝该分类
    def test(self, data):
        count = 0
        for v in self.version_sapce:
            if not self.isConsistent(v, data):
                count -= 1
            else:
                count += 1
        return count

    def isConsistent(self, h, d):
        for idx in h:
            if h[idx]!='?' and d[idx]!=h[idx]:
                return False
        return True

    def getMinih_general(self, h, d, H):
        for idx in h:
            if h[idx]!='?' and h[idx]!=d[idx]:
                if h[idx]=='$':
                    h[idx] = d[idx]
                else:
                    h[idx] = '?'
        for item in H:
            if self.isGeneral(item, h):
                return [h]
        return []

    def getMinih_specific(self, h, d, H, v):
        ret = []

        for idx in h:
            hh = h.copy()
            if hh[idx] =='?':
                for ff in v[idx]:
                    if ff!=d[idx]:
                        hh[idx] = ff
                        ret.append(hh)
                        hh = h.copy()
        idx = 0
        while idx < len(ret):
            f = False
            for item in H:
                if self.isGeneral(ret[idx], item):
                    f  = True
                    break
            if not f:
                ret.pop(idx)
                idx-=1
            idx += 1
        
        return ret

    def checkGeneral(self, H):
        ii = 0
        while ii < len(H):
            h1 = H[ii]
            for jj in range(len(H)):
                if self.isGeneral(h1, H[jj]):
                    H.pop(ii)
                    ii = -1

                    break
            ii += 1

    def isGeneral(self, h1, h2):
        ret = False
        for idx in h1:
            if h1[idx] == '?' and h2[idx]!='?':
                ret = True
            elif h1[idx] =='$' and h2[idx] != '$':
                return False
            elif h1[idx]!=h2[idx]:
                return False
            elif h1[idx]!='$' and h2[idx] =='$':
                ret = True
        return ret

    def GenVp(self):
        for g in self.dG:
            min_specific = self.getMinih_specific(g, g, self.dS, self.values)
            for m in min_specific:
                flag = True
                for v in self.version_sapce:
                    flag = False
                    for key in m:
                        if v[key]!=m[key]:
                            flag = True
                            break
                    if not flag:
                        break
                if flag:
                    self.version_sapce.append(m)
        self.version_sapce.extend(self.dS)
        self.version_sapce.extend(self.dG)



    def PrintTrainResult(self):
        print('set G:')
        print(self.dG)
        print('set S:')
        print(self.dS)
        print('set Vp:')
        print(self.version_sapce)


f = CandidateElimination(ds.getTrainData(), ds.values, 'EnjoySport')

f.train()

print(f.test({'Sky':'Sunny', 'AirTemp':'Warm', 'Humidity':'Normal', 'Wind':'Strong', 'Water':'Cool', 'Forecast':'Change'}))
