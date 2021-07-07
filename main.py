import requests
import random
import urllib
import time # for name
from urllib.request import urlopen # urllib.reuest 'den urlopen'ı çek
from bs4 import BeautifulSoup


def main_process(url,html_or_titletext,number_for_name):

    def formation_of_name_for_files(): # dosyalara random olarak isim vermesi icin
        liste=[]
        x=random.randint(1,100000)
        if x in liste: # eger x liste'nin icindeyse fonksiyonu yeniden cagir
            return formation_of_name_for_files()
        else:
            liste.append(x) #listeye x'i ekle
            name="depth_"+str(number_for_name)+"_data"+str(x)
            return name

    def func_text(url): # to take title an text
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"html.parser")
        title=soup.title.get_text().strip()
        try:
            dosya=open("C:/Users/Ömer/Documents/pyhton_project/"+formation_of_name_for_files()+".txt","w")
            dosya.write(title+"\n"+"********************************************************************")
            sayfa = urllib.request.urlopen(url)
            soup = BeautifulSoup(sayfa, "html.parser")
            ana=soup.find("body")
            alt=ana.findAll("section",attrs={"class":"text-description"})
            for i in alt:
                textt=(i.text.strip())
                try:
                    dosya.write("\n"+textt)
                except UnicodeEncodeError:
                    print()


        except UnboundLocalError:
            textm="\nTHİS PAGE HAS NO TEXT" #sayfada main text olmadiği zaman
            dosya=open("C:/Users/Ömer/Documents/pyhton_project/"+formation_of_name_for_files()+".txt","w")
            dosya.write(title+"\n"+textm)



    def func_html(url): #sayfadan html bilgisi cekmek icin
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"html.parser")
        d=open("C:/Users/Ömer/Documents/pyhton_project/"+formation_of_name_for_files()+".html", "w")
        try:
            d.write(soup.prettify())
        except UnicodeEncodeError:
            print()

    if html_or_titletext==0:
        func_text(url)
    elif html_or_titletext==1:
        func_html(url)
    elif html_or_titletext==2:
        func_text(url)
        func_html(url)
    else:
        print("Try Again ...")









