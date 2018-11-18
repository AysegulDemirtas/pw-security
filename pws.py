#!/usr/bin/env python3
import os
import sys
import math 

#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#      ŞİFRE GÜVENLİĞİ ÖLÇEKLEME ALGORİTMASI v.1      #
#             Yazan: Ayşegül DEMİRTAŞ                 #
#              	Tarih: Temmuz 2017					  #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
print("ŞİFRE GÜVENLİĞİ ÖLÇEKLEME ALGORİTMASI v.1 ")

#proje uzayı küçük harflerin kullanılması temeli üzerine kurulmuştur.
#türkçe karakter kısıtlaması yoktur fakat harf olmayan karakterler(sayılar,noktalama işaretleri vb.) kullanılmamıştır.
alfabe = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']

#boş liste öntanımlaması aşağıdaki gibidir.
içerik = [None] * 1000 ;
sayaç = 0

f= open("kelimeler.txt","r")

if f.mode == 'r':

#içerik = f.read() --> metni bütün olarak okumak için bu formatı kullanabiliriz.
	fline = f.readlines()

	for line in fline:

		içerik[sayaç]=line.split("\n")[0]
		if sayaç == 1000:
			break
		else:
			sayaç = sayaç+1

#içerik listesinin her indisinde bir kelime mevcut. 
#Birleşim gücü yüksek 1000 kelime üzerinde yapılacak olan bu çalışmada içerik yapısını oluşturacak kelimeler bu listede yer almaktadır.  
f.close

#harfsayacı değişkeni kelimeler.txt dosyasında bulunan he sözcükteki harfler toplamıdır.
#harf sayacı +1 fazladan harf sayıyor, nedenini bul !
harfsayacı= 0

for i in içerik:
	harfsayacı = harfsayacı + len(i)

#frekans değişkeni her bir harf için, o harfin içerik tabanında bulunma sıklığını ifade etmektedir.
frekans={}

for harf in alfabe:
	frekansindis=0
	for sözcük in içerik:
		for s in sözcük:	
			if s == harf:
				frekansindis = frekansindis+1
				frekans[harf] = frekansindis

#konum değişkeninde harflerin başta sonda ve ortada bulunma sıklığı değerlendirilir.
konum= {}

başta=[None] * 1000 
sonda=[None] * 1000 
ortada=[None] * (harfsayacı-2000)
iteratorB = 0 
iteratorS = 0 
iteratorO = 0 

for sözcük in içerik:
	for harf in alfabe:
		if sözcük[0] == harf:
			başta[iteratorB] = harf
			iteratorB = iteratorB + 1 
		if sözcük[len(sözcük)-1] == harf:
			sonda[iteratorS] = harf
			iteratorS = iteratorS + 1
	
for sözcük in içerik:	
	indeks=1
	while indeks < len(sözcük)-1:
		for harf in alfabe:	
			if sözcük[indeks] == harf :
				ortada[iteratorO] = harf
				iteratorO = iteratorO + 1
		indeks = indeks + 1

#başta ortada sonda sırasıyla gelmiyor.
#print(konum["k"]["başta"])
for harf in alfabe:
	baş =0
	for b in başta:
		if b == harf:
			baş = baş+1
	
	son =0
	for s in sonda:
		if s == harf:
			son = son+1

	orta =0
	for o in ortada:
		if o == harf:
			orta = orta+1

	konum[harf] = { "başta" : baş ,  "ortada" : orta ,  "sonda" : son}

#birlikte fonksiyonu bir harfin başka bir harfle birlikte tek sözcükte bulunma sayısını verir.
#print(birlikte("b","a"))#şeklinde işlem sonuçlarına ulaşabilirsiniz.
def birlikte(harf1,harf2):
	önbirlikte=[None] * 1000
	önsayı=0
	for sözcük in içerik:
		for s in sözcük:
			var = False
			if harf1 == s:
				var = True
			if var == True :
				for sz in sözcük:
					if sz == harf2 :
						önbirlikte[önsayı] = sözcük
						önsayı = önsayı +1
	birlikte= [None] * önsayı
	sayı=0
	for s in range(önsayı):
		if önbirlikte[s] == önbirlikte[s+1] :
			s = s+1
		else:
			birlikte[sayı] = önbirlikte[s]
			sayı = sayı + 1
			s = s+1
	birlikte = [x for x in birlikte if x is not None]
	return birlikte
		
#yanyana fonksiyonu bir harfin diğer harf ile yanyana bulunma sayısını verir.
#print(yanyana("e","m")) #şeklinde elemanlarına erişilebilir.
def yanyana(harf1,harf2):
	x = 0
	yanyana=[None]*5000
	for sözcük in içerik:
			for s in range(len(sözcük)-1):
				if sözcük[s] == harf1:
					if sözcük[s+1] == harf2:
						yanyana[x]=sözcük
						x= x + 1 
					if s != 0:
						if sözcük[s-1] == harf2:
							yanyana[x]=sözcük
							x= x + 1 
	for i in range(len(yanyana)-1):
		if yanyana[i] == yanyana[i+1]:
			yanyana[i]= None	

	yanyana = [x for x in yanyana if x is not None]
	return yanyana

####USER INTERFACE####KULLANICI ARAYÜZÜ########USER INTERFACE####KULLANICI ARAYÜZÜ####
girdi=input("Lütfen güvenlik derecesini ölçmek istediğiniz kelimeyi girin:")
uzunluk=len(girdi)

kelime = [None]*uzunluk
indeks=0
for g in girdi:
	kelime[indeks]= g
	indeks = indeks +1

#girilen kelimedeki harflerin, sözlük dosyasında bulunma sayıları toplamı : değer1
değer1 = 0
for k in kelime:
	değer1 = değer1 + frekans[k]

#girilen kelimenin ilk harfinin, sözlük dosyasında ilk harf konumunda bulunma sayısı : değer2 
değer2 = konum[kelime[0]]["başta"]

#girilen kelimenin son harfinin, sözlük dosyasında son harf konumunda bulunma sayısı : değer3 
değer3 = konum[kelime[len(kelime)-1]]["sonda"]

#girilen kelimenin ortasındaki harflerin, sözlük dosyasında kelimelerde orta konumda bulunma sayıları toplamı: değer4
değer4=0
for h in range(len(kelime)-2):
	değer4=değer4+ konum[kelime[h+1]]["ortada"]

#girilen kelimedeki her harf için kelimenin içindeki diğer harflerle birlikte, sözlük dosyasında bulunma sayıları toplamı: değer5
birlikteBulunma= [None] * 10000
index = 0 
for klm in kelime:
	for kl in kelime:
		if klm != kl:
			for b in birlikte(klm,kl):
				birlikteBulunma[index]=b
				index = index + 1

birlikteBulunma = [b for b in birlikteBulunma if b is not None]
değer5=len(birlikteBulunma)

#girilen kelimede yanyana bulunanan harflerin, sözlük dosyasında da yanyana bulunma sayıları toplamı: değer6
değer6 = 0 
for i in range(len(kelime)-1):
	değer6 = len(yanyana(kelime[i],kelime[i+1]))

#ölçek katsayıları ile bu 6 değerin çarpılması sonucunda basit bir şifre gücü ölçeği çıkarılıyor.
şifregücü = int( ( (değer1*10) + (değer2*40) + (değer3*40) + (değer4*20) + (değer5*10) + (değer6*30) ) * (0.1) * math.pow(1/uzunluk,2) )
print("Girdiğiniz kelime, dağarcıktaki diğer kelimelerle karşılaştırıldı. \n'" + girdi + "' kelimesinin tahmin edilebilirlik değeri: %s" %şifregücü)
print("Şifre olarak bir kelime seçerken tahmin edilebilirlik değeri düşük kelimeler tercih edilmelidir.")
#################Bitti##################











