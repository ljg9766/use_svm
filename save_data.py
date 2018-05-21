# -*- coding: utf-8 -*-  
import os  
from Data import *
from svmutil import *
import sys

#从数据根路径读取文件夹名为dir, 放在fileCount[dir]的字典,每个fileCount[dir]里为数组,存放的是子文件xls的名称[类别名0:[文件名1,文件名2],类别名1:[文件名1,文件名2],]
def readData(path):
	fileCount = {}	#存放"目录名":["子文件名"]
	             
	#path = 'D:\Motion Classification\JackDrummondMotion_Classifier 2\MotionTest\MotionTest\Test_Data3\\'  

	for i in os.listdir(path):
		dir = i.__str__()
		fileCount[dir] = []


	for key,value in fileCount.items():
		temp_path = path + '\\' + key
		for i in os.listdir(temp_path):
			dir = i.__str__()
			fileCount[key].append(dir)
	return fileCount

#逐个文件读取数据并存放在Data.featureArray里,返回为二维数组[[label,1,2,3...],[label,1,2,3...],[]]
def saveData(path,fileCount):
	for dir in fileCount:
		for filename in fileCount[dir]:
			data = Data()
			data.readFile(path+'\\'+dir+'\\'+filename)
			data.getSampleData(50)
			data.calcMean()
			data.calcStdDevTime()
			if(data.checkValid() == True):
				data.savefeature(int(dir))
	return Data.featureArray

#格式化写入文件	格式为 label 1:data1 2:data2 3:data3 ...
def writeData(featureArray,fileName):			
	file = open(fileName,'w')  
	for feature in featureArray:
		for i in range(0,len(feature)):
			if(i == 0):
				file.write(str(feature[0])+' ')
			else:
				file.write(str(i)+':'+str(feature[i])+' ')
		file.write('\n')
	file.close()  
