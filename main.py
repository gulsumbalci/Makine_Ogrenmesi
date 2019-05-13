# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 17:36:48 2017

@author: GULSUM
"""

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

from tasarim import Ui_Form

class MainWindow(QtGui.QMainWindow, Ui_Form):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.btn_knn_goster.clicked.connect(self.knnGoster)
        self.btn_knn_siniflandir.clicked.connect(self.knnSiniflandir)
        self.btn_kmeans_goster.clicked.connect(self.kmeansGoster)
        self.btn_kmeans_kumele.clicked.connect(self.kmeansKumele)
        self.btn_knn_kume1.clicked.connect(self.dataOlustur)
        self.radio_oklid.clicked.connect(self.Knn_Oklid_Kumele)
        self.radio_minkowski.clicked.connect(self.Knn_Minkowski_Kumele)
        self.radio_manhattan.clicked.connect(self.Knn_Manhattan_Kumele) 
        self.btn_naive.clicked.connect(self.naiveBayesAlgoritma)        
        
    def knnGoster(self):
        verilistesi =[]
        verilistesi.append((2,4,"kotu"))
        verilistesi.append((3,6,"kotu"))
        verilistesi.append((3,4,"iyi"))
        verilistesi.append((4,10,"kotu"))
        verilistesi.append((5,8,"kotu"))
        verilistesi.append((6,3,"iyi"))
        verilistesi.append((7,9,"iyi"))
        verilistesi.append((9,7,"kotu"))
        verilistesi.append((11,7,"kotu"))
        verilistesi.append((10,2,"kotu"))
        renk=""
        maks=self.max_deger(verilistesi)+1
        for m in verilistesi:
            if m[2]=="kotu":
                renk="ro"
                plt.plot(int(m[0]),int(m[1]),renk)
            elif m[2]=="iyi": 
                renk="bo"
                plt.plot(int(m[0]),int(m[1]),renk)
        plt.plot(int(self.txt_x.text()),int(self.txt_y.text()),"yo")
        plt.axis([0, maks, 0, maks])
        path="./resimler/knn_once.png"
        plt.savefig(path)
        self.image_show(path,self.resim_goster)
    
    def knnSiniflandir(self):
        verilistesi =[]
        verilistesi.append((2,4,"kotu"))
        verilistesi.append((3,6,"kotu"))
        verilistesi.append((3,4,"iyi"))
        verilistesi.append((4,10,"kotu"))
        verilistesi.append((5,8,"kotu"))
        verilistesi.append((6,3,"iyi"))
        verilistesi.append((7,9,"iyi"))
        verilistesi.append((9,7,"kotu"))
        verilistesi.append((11,7,"kotu"))
        verilistesi.append((10,2,"kotu"))
        kotu=0
        iyi=0
        
        x=int(self.txt_x.text() )
        y=int(self.txt_y.text())
        k=int(self.txt_k.text())
        
        uzakliklarlistesi= []
        for m in verilistesi:
            uzunluk = sqrt((x-m[0])**2 + (y-m[1])**2)
            durum= m[2]
            uzakliklarlistesi.append((uzunluk,durum))
        for m in range (0,len(uzakliklarlistesi)-1):
            for n in range(m,len (uzakliklarlistesi)):
                if uzakliklarlistesi[m]>uzakliklarlistesi[n]:
                    tmp = uzakliklarlistesi[m]
                    uzakliklarlistesi[m] = uzakliklarlistesi[n]
                    uzakliklarlistesi[n]=tmp
        uzakliklarlistesi.sort()
        for i,row in enumerate(uzakliklarlistesi):
            if i==k:
                break
            else:
                if row[1] =='kotu':
                    kotu +=1
                else :
                     iyi +=1

        if kotu > iyi: 
           self.lbl_bilgi.setText("kotu")
           verilistesi.append((x,y,"kotu"))
        else: 
          self.lbl_bilgi.setText("iyi")
          verilistesi.append((x,y,"iyi"))
        maks=self.max_deger(verilistesi)+1
        for m in verilistesi:
            if m[2]=="kotu":
                renk="ro"
                plt.plot(int(m[0]),int(m[1]),renk)
            elif m[2]=="iyi": 
                renk="bo"
                plt.plot(int(m[0]),int(m[1]),renk)
        plt.axis([0, maks, 0, maks])
        path="./resimler/knn_sonra.png"
        plt.savefig(path)
        self.image_show(path,self.resim_goster2)
        
    def image_show(self,file_name,gosterme_yeri):
        w,h=gosterme_yeri.width()-5,gosterme_yeri.height()-5
        pixMap = QtGui.QPixmap(file_name) 
        pixMap=pixMap.scaled(w,h)            
        pixItem = QtGui.QGraphicsPixmapItem(pixMap)
        scene2 = QGraphicsScene()
        scene2.addItem(pixItem)       
        gosterme_yeri.setScene(scene2)
    
    def max_deger(self,liste):
        value=max(liste)
        maxVal=0
        if value[0]>value[1]:
            maxVal=value[0]
        else:
            maxVal=value[1]
        
        return maxVal
    
    def kmeansGoster(self):
        veriListesi1=[]
        veriListesi1.append((4,2,"c1"))
        veriListesi1.append((6,4,"c1"))
        veriListesi1.append((5,1,"c2"))
        veriListesi1.append((10,6,"c1"))
        veriListesi1.append((11,8,"c2"))
        renk=""
        maks=self.max_deger(veriListesi1)+1
        for m in veriListesi1:
            if m[2]=="c1":
                renk="ro"
                plt.plot(int(m[0]),int(m[1]),renk)
            elif m[2]=="c2": 
                renk="bo"
                plt.plot(int(m[0]),int(m[1]),renk)
        plt.plot(int(self.txt_x2.text()),int(self.txt_y_2.text()),"go")
        plt.axis([0, maks, 0, maks])
        path="./resimler/kmeans_once.png"
        plt.savefig(path)
        self.image_show(path,self.resim_goster)
        
    def kmeansKumele(self):
        veriListesi=[]
        veriListesi.append((4,2,"c1"))
        veriListesi.append((6,4,"c1"))
        veriListesi.append((5,1,"c2"))
        veriListesi.append((10,6,"c2"))
        veriListesi.append((11,8,"c2"))
        veriListesi.append((4,8,"c1"))
        veriListesi.append((5,6,"c2")) 
        x=int(self.txt_x2.text())
        y=int(self.txt_y_2.text())
        etiket=self.combo_kmeans.currentText()
        veriListesi.append((x,y,etiket))
        self.islem_Kmeans(veriListesi)
        
    def islem_Kmeans(self,veriListesi1):
        c1x=0.0
        c2x=0.0
        c1s=0
        c1y=0.0
        c2y=0.0
        c2s=0    
        for m in veriListesi1:
            if m[2]=="c1":
                c1s=c1s+1
                c1x=c1x+m[0]
                c1y=c1y+m[1]
            else :
                c2s=c2s+1
                c2x=c2x+m[0]
                c2y=c2y+m[1]                
        c1merkez=[]
        c2merkez=[]    
        c1merkez.append((c1x/c1s, c1y/c1s))
        c2merkez.append((c2x/c2s,c2y/c2s))
        yeniliste=[]    
        c1uzaklik=0
        c2uzaklik=0
        
        for m in veriListesi1:
            c1uzaklik=sqrt(pow((int(m[0])-c1merkez[0][0]),2)+pow((int(m[1])-c1merkez[0][1]),2))
            c2uzaklik=sqrt(pow((int(m[0])-c2merkez[0][0]),2)+pow((int(m[1])-c2merkez[0][1]),2))
            if (c1uzaklik>c2uzaklik):
                yeniliste.append(("c2"))
            else :
                yeniliste.append(("c1"))   
        degisim=0
        sonListe=[]
    
        for p in range(0,len(yeniliste)):
            if yeniliste[p]==veriListesi1[p][2]:
                sonListe.append(veriListesi1[p])
            else:
                sonListe.append((veriListesi1[p][0],veriListesi1[p][1],yeniliste[p]))
                degisim=degisim+1
        
        if degisim!=0:
            self.islem_Kmeans(sonListe)
        else:
            for d in sonListe:
                print (d)
            maks=self.max_deger(veriListesi1)+1
            for m in sonListe:
                if m[2]=="c1":
                    renk="ro"
                    plt.plot(int(m[0]),int(m[1]),renk)
                elif m[2]=="c2": 
                    renk="bo"
                    plt.plot(int(m[0]),int(m[1]),renk)
            plt.axis([0, maks, 0, maks])
            path="./resimler/kmeans_sonra.png"
            plt.savefig(path)
            self.image_show(path,self.resim_goster2)
            
    def randomData(self,maksDeger,count):
        data = np.random.random_integers(0, maksDeger, count*2).reshape((count,2))
        return data
    def dataOlustur(self):
        veri=self.randomData(100,40)
        for nokta in veri:
            plt.plot(int(nokta[0]),int(nokta[1]),"ro")   
        plt.axis([0, 100, 0, 100]) #bura değişecek
        plt.title("Veri Seti Ilk hali")
        path="./resimler/knn_kümelenmeden_once.png"
        plt.savefig(path)
        self.image_show(path,self.resim_goster)

    def oklid_liste(self,ref,verilistesi):
        dataset=verilistesi
        veri=[]
        for j in dataset:
            veri.append((sqrt(pow((ref[0]-j[0]),2)+pow(ref[1]-j[1],2)))) #noktaların öklid uzaklıkları
        return veri                
    def oklid_sifir(self,verilistesi):
        dataset=verilistesi
        veri=[]
        for i in dataset:
            veri.append(((sqrt(pow((i[0]-0),2)+pow(i[1]-0,2))),i))
        veri=sorted(veri, key=lambda veri: veri[0])
        return veri
        
    def minkowski_liste(self,ref,verilistesi):
        dataset=verilistesi
        veri=[]
        for j in dataset:
            bisey=(pow(abs(ref[0]-j[0]),3)+pow(abs(ref[1]-j[1]),3))
            mnk=pow(bisey,0.33)
            veri.append(mnk)
        return veri 
    def minkowski_sifir(self,verilistesi):
        dataset=verilistesi
        veri=[]
        for j in dataset:
            bisey=(pow(abs(j[0]-0),3)+pow(abs(j[1]-0),3))
            mnk=pow(bisey,0.33)
            veri.append((mnk,j))
        return veri 
        
    def manhattan_liste(self,ref,verilistesi):
        dataset=verilistesi
        veri=[]
        for j in dataset:
            veri.append((abs(ref[0]-j[0])+abs(ref[1]-j[1]))) #noktaların manhattan uzaklıkları 
        return veri     
    def manhattan_sifir(self,verilistesi):
        dataset=verilistesi
        veri=[]
        for j in dataset:
            veri.append(((abs(j[0]-0)+abs(j[1]-0)),j)) 
        return veri 
        
    def gruplandir(self,dataset,uzakliksifir,currentIndex):
        son=len(uzakliksifir)-1
        a1=[]
        b1=[]
        a_ref=uzakliksifir[0][1]
        b_ref=uzakliksifir[son][1]    
        
        if currentIndex==0: # oklid
            for a in dataset:
                a_list=self.oklid_liste(a_ref,dataset)
                b_list=self.oklid_liste(b_ref,dataset)
            for i in range (0,len(a_list)):
                if a_list[i] >b_list[i]:
                    b1.append((dataset[i]))
                else:
                    a1.append((dataset[i]))
                    
        elif currentIndex==1: #manhattan
            for a in dataset:
                a_list=self.manhattan_liste(a_ref,dataset)
                b_list=self.manhattan_liste(b_ref,dataset)
            for i in range (0,len(a_list)):
                if a_list[i] >b_list[i]:
                    b1.append((dataset[i]))
                else:
                    a1.append((dataset[i]))
        elif currentIndex==2:#minkowski
            for a in dataset:
                a_list=self.minkowski_liste(a_ref,dataset)
                b_list=self.minkowski_liste(b_ref,dataset)
            for i in range (0,len(a_list)):
                if a_list[i] >b_list[i]:
                    b1.append((dataset[i]))
                else:
                    a1.append((dataset[i]))
        
        for m in a1:
            renk='ro'
            plt.plot(int(m[0]),int(m[1]),renk)
        for m in b1:
            renk='bo'
            plt.plot(int(m[0]),int(m[1]),renk)
        
        plt.axis([0, 100, 0, 100]) #bura değişecek
        plt.title("Veri Seti Ilk hali")
        path="./resimler/knn_kumelemeden_sonra.png"
        plt.savefig(path)
        self.image_show(path,self.resim_goster2)
    #    plt.savefig("./kmeans_ilk.png")    
    
#    def knnOklidUzaklık(self):
#        self.gruplandir(data,oklid_sifir(data),0)
    def Knn_Oklid_Kumele(self):
        data=self.randomData(100,40)
        self.gruplandir(data,self.oklid_sifir(data),0)
    def Knn_Minkowski_Kumele(self):
        data=self.randomData(100,40)
        self.gruplandir(data,self.minkowski_sifir(data),2)
    def Knn_Manhattan_Kumele(self):
        data=self.randomData(100,40)
        self.gruplandir(data,self.manhattan_sifir(data),1)
    
    def KategoriSayisi(self,kume, kelime, index):
        counter=0
        for i in range(len(kume)):
            if kume[i][index]==kelime:
                counter+=1
        return counter
        
    def kelime_kontrol(self,kume, kelime):
        counter=0
        for i in range(len(kume)):
            if kume[i]==kelime:
                counter+=1
        return counter
        
    def kelimeler(self,kume):
        kelimeler=[]
        silinecek="!@#$.?,"
        for i in range(len(kume)):
            cumle=kume[i][0]
            for char in silinecek:
                cumle=cumle.replace(char,"")
            parca=cumle.split(' ')
            for c in parca:
                if self.kelime_kontrol(kelimeler, c)==0:
                    kelimeler.append(c)
        return kelimeler
        
    def arama(self,kume,kumeci,kelime):
        counter=0
        for i in range(len(kume)):
            if kume[i][1]==kumeci and kume[i][0].count(kelime)>0:
                counter+=kume[i][0].count(kelime)
        return counter
    def naiveBayesAlgoritma(self):
        data=[["mause , fare. kulaklik. klavye","Bigisayar"],
            ["mause. , fare@ kulaklik sarj","Bilgisayar"],
            ["silgi defter.","Kirtasiye"],
            ["kitap? kalem","Kirtasiye"],
            ["canta. kulaklik sarj","Kirtasiye"]]
            
        kelime=self.txt_metin.text()
        
        countham=self.KategoriSayisi(data,"Bigisayar",1)
        countspam=self.KategoriSayisi(data,"Kirtasiye",1)
        hamagirlik=float(countham)/(float(countham)+float(countspam))
        spamagirlik=float(countspam)/(float(countham)+float(countspam))
        kelimeci=self.kelimeler(data)
        hmtoplam=0
        hmdeger=[]
        for i in kelimeci:
            hmtoplam+=(self.arama(data,"Bigisayar",i)+1)
        
        for i in range(len(kelimeci)):
            deger=float(self.arama(data,"Bigisayar",kelimeci[i])+1)/float(hmtoplam)
            hmdeger.append(deger)
            
        spmtoplam=0
        spmdeger=[]
        for i in kelimeci:
            spmtoplam+=(self.arama(data,"Kirtasiye",i)+1)
        
        for i in range(len(kelimeci)):
            deger=float(self.arama(data,"Kirtasiye",kelimeci[i])+1)/float(spmtoplam)
            spmdeger.append(deger)
            
        c_kelime=kelime.split(" ")
        hmcarpim=1
        for i in c_kelime:
            for x in range(len(kelimeci)):
                if kelimeci[x]==i:
                    hmcarpim*=hmdeger[x]
        
        spmcarpim=1
        for i in c_kelime:
            for x in range(len(kelimeci)):
                if kelimeci[x]==i:
                    spmcarpim*=spmdeger[x]
        
        hmsonuc=hmcarpim*hamagirlik
        spmsonuc=spmcarpim*spamagirlik
        
        if hmsonuc<spmsonuc:
            self.lbl_naive.setText("kategori Kirtasiye")
        else:
            self.lbl_naive.setText("kategori Bilgisayar")
            