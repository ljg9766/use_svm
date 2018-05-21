import os
import sys
from svmutil import *

#os.chdir('D:\libsvm-3.22\python')

#训练数据
def train(problemPath,modelName):
	y,x = svm_read_problem(problemPath)
	m = svm_train(y[0:], x[0:], '-b 1')
	svm_save_model(modelName, m)
	p_label, p_acc, p_val = svm_predict(y[0:], x[0:], m,'-b 1')
	print("对应测试结果:")
	print(p_label)
	print("准确率,误差的均方差,相关系数平方")
	print(p_acc)
	print("***********")
	print(p_val)

#文件预测数据
def filePredict(filePath,modelName):
	y,x = svm_read_problem(filePath)
	m = svm_load_model(modelName)
	p_label, p_acc, p_val = svm_predict(y[0:], x[0:], m,'-b 1')
	print("对应测试结果:")
	print(p_label)
	print("准确率,误差的均方差,相关系数平方")
	print(p_acc)
	print("***********")
	print(p_val)

#预测数组数据
def listPredict(labels,datas,modelName):
#	pros = svm_problem(labels,datas)
	m = svm_load_model(modelName)
	p_label, p_acc, p_val = svm_predict(labels,datas, m,'-b 1')
	print("对应测试结果:")
	print(p_label)
	print("预测准确率,误差的均方差,相关系数平方")
	print(p_acc)
	print("***********")
	print(p_val)
	return p_label,p_acc,p_val
#四.额外计算准确率 
# ACC, MSE, SCC = svmutil.evaluations(true_val, predict_val)     predict是个一维数组[]