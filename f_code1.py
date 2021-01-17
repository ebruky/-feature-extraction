# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:51:21 2020

@author: ebruk
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout,QDesktopWidget, QWidget,QTableWidget,QTableView,QTableWidgetItem,QHeaderView,QGraphicsScene,QGraphicsPixmapItem,QFileDialog
import pandas as pd
import openpyxl
import math
import random
import numpy as np
import xlwt
from f_tasarim1 import Ui_Dialog
from sklearn.externals import joblib
from skimage import io
import os
from skimage.transform import resize
from skimage import feature
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix



class MainWindow(QWidget,Ui_Dialog):

    liste=["kedi","kopek"]
    veriler=[]
    resim_yolu=""
    x=[]
    targets=[]
    
   
    
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.verileriYukle.clicked.connect(self.yukle)
        self.images.clicked.connect(self.resim_yukle)
        self.algoritma.activated[str].connect(self.seciliAlgoritma)
        im=["Random Forest","Decision Tree","Logistic Regression"]
        for i in im:         
            self.algoritma.addItem(i)
        
    def yukle(self):
        self.veriler=[]
        k=-1
        for i in self.liste:
            k+=1
            file_path='./resimler/'+i+'/'
            files=os.listdir(file_path)
            self.x=[]
            self.targets=[]
            for file in files:
                y=self.liste.index(i)
                img=io.imread(file_path+file)
                w,h=img.shape[:2]
                self.images.insertItem(k, file)
                feature_matrix=np.zeros((w,h))
                for a in range(w):
                    for b in range(h):
                        feature_matrix[a,b]=(img[a,b][0]+img[a,b][1]+img[a,b][2])/3
                features=feature_matrix.reshape((w*h))
                
                self.x.append(features)
                self.targets.append(y)
                self.veriler.append([features,y])
                
        self.data.clear()
        self.data.setColumnCount(2)
        self.data.setRowCount(len(self.veriler))
        columnListe=[]
        for c in range(0,2):
          columnListe.append(str(c))
        self.data.setHorizontalHeaderLabels(columnListe)
        for i,row in enumerate(self.veriler):
         for j,cell in enumerate(row):
           self.data.setItem(i,j, QTableWidgetItem(str(cell)))

    def resim_yukle(self, qmodelindex):
        item = self.images.currentItem()
        for i in self.liste:
            file_path='./resimler/'+i+'/'
            files=os.listdir(file_path)
            for file in files:
                if item.text()==file:
                    self.resim_yolu=str(file_path+file)
                    break
                    
        print(self.resim_yolu)
        self.secilen_img.setPixmap(QtGui.QPixmap(self.resim_yolu))
        
        
        
       
    def seciliAlgoritma(self,text):
        
        model=""
        if text=="Random Forest":
            model=RandomForestClassifier(n_estimators=self.x.shape[0])
        elif text=="Decision Tree":
            model=DecisionTreeClassifier()
        else:
            model=LogisticRegression()
        
        self.basariBul(model)
        
    def basariBul(self,m):
        self.x=np.array(self.x)
        
        X_train, X_test, y_train, y_test = train_test_split(self.x, self.targets, test_size=0.2,random_state=42)
       
        m.fit(X_train,y_train)
        tahminler=m.predict(X_test)
        ds,ys,snc=0,0,0
        for i in range (len(tahminler)):
            if y_test[i]==tahminler[i]:
                ds+=1
            else:
                ys+=1
        snc= round(float(ds/(ds+ys))*100,2)
        self.basari.setText(str(snc))
        
        y_true = y_test
        y_pred = tahminler
        self.lineEdit.setText(str(confusion_matrix(y_true, y_pred)))
        
        
        
        
                
        
        