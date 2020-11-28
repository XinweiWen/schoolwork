# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 2020

subject:朴素贝叶斯分类
"""

from sklearn import naive_bayes
from sklearn.datasets import load_digits
from sklearn.model_selection  import train_test_split


#导入数据集
def load_data():
    digits = load_digits()
    X_train = digits.data
    y_train = digits.target
    return train_test_split(X_train,y_train, test_size=0.25,random_state=0,stratify=y_train)
 

#定义高斯朴素贝叶斯分类函数 
def test_GaussianNB(*data):
    X_train,X_test,y_train,y_test=data
    cls=naive_bayes.GaussianNB()
    cls.fit(X_train,y_train)
    print('GaussianNB Train score :%.2f'%cls.score(X_train,y_train))
    print('GaussianNB Test score :%.2f'%cls.score(X_test,y_test))

#定义多项式朴素贝叶斯分类函数 
def test_MultinomialNB(*data):
    X_train,X_test,y_train,y_test=data
    cls = naive_bayes.MultinomialNB()
    cls.fit(X_train,y_train)
    print('MultinomialNB Train score :%.2f'%cls.score(X_train,y_train))
    print('MultinomialNB Test score :%.2f'%cls.score(X_test,y_test))
 
#定义伯努利朴素贝叶斯分类函数  
def test_BernoulliNB(*data):
    X_train,X_test,y_train,y_test = data
    cls=naive_bayes.BernoulliNB()
    cls.fit(X_train,y_train)
    print('BernoulliNB Train score :%.2f'%cls.score(X_train,y_train))
    print('BernoulliNB Test score :%.2f'%cls.score(X_test,y_test))
 
if __name__=='__main__':
    X_train,X_test,y_train,y_test = load_data()
    test_GaussianNB(X_train,X_test,y_train,y_test)
    test_MultinomialNB(X_train,X_test,y_train,y_test)
    test_BernoulliNB(X_train,X_test,y_train,y_test)