"""
#Python
#title 		:Data_Scraping.py
#description:This is a web data scraper app
#author 	:JohnBedeir
#website	:johnydesigns.com
#date		:27Oct20
"""


from tkinter import *
import requests
from bs4 import BeautifulSoup
import pandas

window=Tk()
window.title("Souq.com Data Scraper")

def Export():
    r=requests.get(e1_text.get())
    c=r.content     
    soup=BeautifulSoup(c, "html.parser")
    all=soup.find_all("div",{"class":"column column-block block-list-large single-item"})
    l=[]
    for item in all:
        d={}
        d["Name"]=item.find("h1",{"class","itemTitle"}).text.replace("\n\t\t\t","")
        d["Price"]=item.find("h3",{"class","itemPrice"}).text
        l.append(d)
        df=pandas.DataFrame(l)
        df.to_csv("File.csv")


def Show_Data():
    r=requests.get(e1_text.get())
    c=r.content     
    soup=BeautifulSoup(c, "html.parser")
    all=soup.find_all("div",{"class":"column column-block block-list-large single-item"})
    for item in all:
        Name=item.find("h1",{"class","itemTitle"}).text.replace("\n\t\t\t","")
        Price=item.find("h3",{"class","itemPrice"}).text
        t1.insert(END, Name)
        t2.insert(END, Price)

#LABELS
l1=Label(window, text="Type the URL")
l1.grid(row=0,column=1)
l2=Label(window, text="Item Name")
l2.grid(row=3,column=0)
l3=Label(window, text="Item Price")
l3.grid(row=3,column=2)

#ENTERIES
e1_text=StringVar()
e1=Entry(window, textvariable=e1_text)
e1.grid(row=1, column=1)


#BUTTONS
b1=Button(window, text="Show Data", command=Show_Data)
b1.grid(row=1,column=0)
b2=Button(window, text="Export", command=Export)
b2.grid(row=1,column=2)


#TEXTAREA
t1=Listbox(window)
t1.grid(row=4,column=0)
t2=Listbox(window)
t2.grid(row=4,column=2)


#SCROLLBAR
sb1=Scrollbar(window)
sb1.grid(row=4,column=1)
t1.configure(yscrollcommand=sb1.set)
sb1.configure(command=t1.yview)

sb2=Scrollbar(window)
sb2.grid(row=4,column=3)
t2.configure(yscrollcommand=sb2.set)
sb2.configure(command=t2.yview)

window.mainloop()