import save_data 
import svm_file_predict
from Data import *
import sys


def predict(path):
	#path = 'D:\Motion Classification\JackDrummondMotion_Classifier 2\MotionTest\MotionTest\\Test_Data3\\lixiaohu_0 2016-01-04 14-26-09.csv'
	label = [0]
	feature = []
	data = Data()
	data.readFile(path)
	data.getSampleData(50)
	data.calcMean()
	data.calcStdDevTime()
	if(data.checkValid() == True):
		tem_feature = data.savefeature(path)
		feature.append(tem_feature)
	print(label)
	print(feature)
	p_label,p_acc,p_val = svm_file_predict.listPredict(label,feature,'svm_test_1.model')
	return p_label

if __name__ == "__main__":
	p_label = predict(sys.argv[1])
	print(p_label)
	#测试save_data
	#保存为格式化文件
	# path = 'D:\Motion Classification\JackDrummondMotion_Classifier 2\MotionTest\MotionTest\Test_Data' 

	# path = 'D:\Motion Classification\JackDrummondMotion_Classifier 2\MotionTest\MotionTest\\all' 

	# fileCount = save_data.readData(path)
	# featureArray = save_data.saveData(path,fileCount)
	# save_data.writeData(featureArray,'data_format_all.txt')

	# 测试svm_file_predict
	#根据格式化文件训练后保存为model
	# path = r'C:\Users\Administrator\Desktop\其他\python\svm_python\svm_motion'
	# dataFile = 'data_format_all.txt'
	# path+='\\'+dataFile
	# svm_file_predict.train(path,'svm_test_1.model')

	#格式化文件的预测
	# dataFile = 'data_format.txt' 
	# #dataFile = 'testing_data_libSVM.dat'
	# dataFile = 'data_format_all.txt'
	# filePath = r'C:\Users\Administrator\Desktop\其他\python\svm_python\svm_motion' + '\\' + dataFile
	# svm_file_predict.filePredict(dataFile,'svm_test_1.model')

	#数组类型的预测
	# labels = [0]
	# datas = [[0.208345,-0.419316,0.734208,0.82428,0.232169,0.338345,0.437932,0.075616,0.048224,0.02994,0.095478,0.073746]] #0
	# #datas = [[1.024459,0.093364,-0.26975,1.02762,-0.20868,-0.207705,0.013286,0.071784,0.033488,0.0095,0.037883,0.035833]] #1
	# #datas = [[0.232649,-0.545877,0.763939,0.683606,0.10702,0.591234,0.420613,0.061017,0.018131,0.01386,0.017997,0.010536]] #3
	# svm_file_predict.listPredict(labels,datas,'svm_test.model')
	