import csv

#类定义
class Data:
   
    __MIN_STD = 1E-9
    __VALID_THRESHOLD = 2
    goodCount = 0 #有效数据数
    width = 0 #数据宽度,即列数
    featureArray = [] #所有的数据特征(类别,平均数、标准差)数组
    first = True #第一次读取文件的标志
    def __init__(self):
         #变量
        # __path = ""
        self.__test_data = [] #单个文件的数据
        self.__sample_data = [] #抽样后的数据数组
        self.__meanArray = [] #单个文件的每列数据的平均数数组
        self.__stdDevTimeArray = [] #单个文件的每列数据的标准差数组
        self.length = 0 #单个文件的抽样后的数据长度
       
    #函数
    #读取文件数据放入test_data数组内
    def readFile(self,path):
        # self.__path = path
        with open(path,'r') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:  #按每行读取文件
                if(Data.first == True):#第一次读取文件时确定width
                    Data.width = len(row)
                    Data.first = False
                # tmp_data = [] #列数组
                # for i in range(0,len(row)): #在同一行内逐个读取数据
                #     tmp_data.append(row[i]) #将数据放入列数组内
                self.__test_data.append(row)#将列数组放入行数组内[[1,2,..,6],[],[]]
    #获取抽样数据 只需第一列抽样, todo 待优化
    def getSampleData(self,downsampleRate):
        downTemp = 0
        for i in range(0,Data.width):
            for j in range(0,len(self.__test_data),downsampleRate):
                self.__test_data[downTemp][i] = self.__test_data[j][i]
                if(i == 0):
                    self.__sample_data.append(self.__test_data[downTemp])
                    downTemp+=1
        self.length = downTemp
        return self.__sample_data

    
    #求样本每列数据的平均数并保存在meanArray数组内
    def calcMean(self):
        for column in range(0,len(self.__sample_data[0])):  #循环每一列
            sum = 0
            for row in self.__sample_data: #遍历数组
                sum = round(sum+float(row[column]),6)#求和
            self.__meanArray.append(round(sum/float(len(self.__sample_data)),6)) #将平均数放入平均数数组内
    
        return self.__meanArray #返回平均数数组

    #求样本每列数据的标准差并保存在stdDevTimeArray数组内
    def calcStdDevTime(self):
        for column in range(0,len(self.__sample_data[0])):  #循环每一列
            stdDevTime = 0.0
            for row in self.__sample_data: #遍历数组
                stdDevTime = round(stdDevTime + pow(float(row[column]) - self.__meanArray[column],2.0),6)
            self.__stdDevTimeArray.append(round(pow(stdDevTime/float(len(self.__sample_data)),0.5),6)) #将标准差放入标准差数组内

        return self.__stdDevTimeArray #返回标准差数组

    def savefeature(self,lable):
        feature = [] #单个文件的特征值数组
        for mean in self.__meanArray: #遍历平均值数组，将该文件的平均值存入特征值数组内
            feature.append(mean)
        for stdDevTime in self.__stdDevTimeArray:  #遍历标准差数组，将该文件的标准差存入特征值数组内
            feature.append(stdDevTime)
        Data.featureArray.append(feature) #将该文件的特征值数组存入总特征数组中
        Data.goodCount+=1

        return feature
 
    def getfeature(self):
        return Data.featureArray #返回总特征数组和标签数组

    #验证数据有效性
    def checkValid(self):
        validCheck = 0;
        valid = True
        for stdDevTime in self.__stdDevTimeArray:
            if(stdDevTime < Data.__MIN_STD):
                validCheck+=1

        if(validCheck < Data.__VALID_THRESHOLD):
            valid = True
        else:
            valid = False

        validCheck = 0

        if(valid == True):
            for i in range(0,Data.goodCount):
                validCheck = 0
                for j in range(0,Data.width):
                    if(self.__meanArray[j] - Data.featureArray[i][j+1] < 1e-6):
                        validCheck+=1
                    if(self.__stdDevTimeArray[j] - Data.featureArray[i][j+1+Data.width] < 1e-6):
                        validCheck+=1

            if(validCheck == 2*Data.width):
                valid = False

        return valid
