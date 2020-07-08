from pandas import read_csv, read_excel
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import pandas as pd
# df = pd.read_excel('C:\\Users\\hxb\\Downloads\\总部账目 - 代理货款.xlsx')
filename = read_excel('C:\\Users\\hxb\\Downloads\\总部账目 - 代理货款.xlsx')

names = ['姓名', '手机号', '代理等级', '上级姓名', '上级手机号', '上级等级', '货款余额', '充值中货款']
data = filename.head(100)
data1 = filename.values
print(format(data))