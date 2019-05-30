from tkinter import *
import time
import imagesize
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from tkinter import ttk
from PIL import Image, ImageTk
#import pylint
master=Tk()
master.geometry("300x180")
label=Label(master,text="Search Bar",fg="white",bg="#343434",font=('Arial',20,'bold'))
label.pack(side=TOP)
textin=""
textin=StringVar()
master.configure(bg="#343434")
def Search1():
    global textin
    global e
    e=str(textin.get())
def clrbtr():
    global e
    global textin
    textin.set("")
def clrbtr1(event):
    global e
    global textin
    textin.set("")
v= IntVar()

def search12():
    Search1()
    if e =="":
        global textin
        textin.set("Error!!! Please Type something")
    else:
    
        if(v.get()==1):
            driver=webdriver.Chrome(executable_path="D:/selenium driver/chromedriver_win32/chromedriver.exe")
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get("https://www.google.com/")
            driver.find_element_by_name("q").send_keys(e)
            time.sleep(2)
            driver.find_element_by_name("btnk").send_keys(Keys.ENTER)
            time.sleep(5)
        elif(v.get()==2):
            driver=webdriver.Chrome(executable_path="D:/selenium driver/chromedriver_win32/chromedriver.exe")
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get("https://www.youtube.com/")
            driver.find_element_by_id("search").send_keys(e)
            time.sleep(2)
            driver.find_element_by_id("search-icon-legacy").send_keys(Keys.ENTER)
            time.sleep(5)
        elif(v.get()==3):
            driver=webdriver.Chrome(executable_path="D:/selenium driver/chromedriver_win32/chromedriver.exe")
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get("https://www.amazon.com/")
            driver.find_element_by_id("twotabsearchtextbox").send_keys(e)
            time.sleep(2)
            driver.find_element_by_class_name("nav-input").send_keys(Keys.ENTER)
            time.sleep(5)
        elif(v.get()==4):
            driver=webdriver.Chrome(executable_path="D:/selenium driver/chromedriver_win32/chromedriver.exe")
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get("https://www.flipkart.com/")
            driver.find_element_by_name("q").send_keys(e)
            time.sleep(2)
            driver.find_element_by_class_name("_2BhAHa").send_keys(Keys.ENTER)
            time.sleep(5)
        else:
            #global textin
            textin.set("Error!!! Please Select Appropriate Browser")
        
       
def search123(event):
    Search1()
    if e =="":
        global textin
        textin.set("Error!!! Please Type something")
    else:
    
        if(v.get()==1):
            driver=webdriver.Chrome(executable_path="D:/selenium driver/chromedriver_win32/chromedriver.exe")
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get("https://www.google.com/")
            driver.find_element_by_name('q').send_keys(e)
            time.sleep(2)
            driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
            time.sleep(5)
        elif(v.get()==2):
            driver=webdriver.Chrome(executable_path="D:/selenium driver/chromedriver_win32/chromedriver.exe")
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get("https://www.youtube.com/")
            driver.find_element_by_id("search").send_keys(e)
            time.sleep(2)
            driver.find_element_by_id("btnk").send_keys(Keys.ENTER)
            time.sleep(5)
        elif(v.get()==3):
            driver=webdriver.Chrome(executable_path="D:/selenium driver/chromedriver_win32/chromedriver.exe")
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get("https://www.amazon.com/")
            driver.find_element_by_id("twotabsearchtextbox").send_keys(e)
            time.sleep(2)
            driver.find_element_by_class_name("nav-input").send_keys(Keys.ENTER)
            time.sleep(5)
        elif(v.get()==4):
            driver=webdriver.Chrome(executable_path="D:/selenium driver/chromedriver_win32/chromedriver.exe")
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.get("https://www.flipkart.com/")
            driver.find_element_by_name("q").send_keys(e)
            time.sleep(2)
            driver.find_element_by_class_name("_2BhAHa").send_keys(Keys.ENTER)
            time.sleep(5)
        else:
            #global textin
            textin.set("Error!!! Please Select Appropriate Browser")
mt=Entry(master,font=("arial",12,'bold'),bd=4,textvariable=textin,width=30,bg='white',fg='black')
mt.place(x=0,y=40)
clrimg=PhotoImage(file="download3.png")
c1=clrimg.subsample(10,10)
butclr=Button(master,command=clrbtr ,image=clrimg,font=("Monospace",12))
butclr.place(x=270,y=40)
butclr.configure(image=c1)
serimg=PhotoImage(file="s2.png")
s1=serimg.subsample(15,15)
butser=Button(master,padx=2,pady=1,bd=0,width=65,bg='powder blue',fg='#343434',command=search12 ,text="search",image=serimg,compound=LEFT,font=("Monospace",12))
butser.place(x=100,y=75)
butser.configure(image=s1)

master.bind('<Return>', search123)
master.bind('<Escape>', clrbtr1)

Radiobutton(master,text="Google",padx = 20,fg="white",bg="#343434",variable=v,value=1,selectcolor="#343434").place(x=10,y=100)
Radiobutton(master,text="Youtube",padx = 20,fg="white",bg="#343434",variable=v,value=2,selectcolor="#343434").place(x=10,y=130)
Radiobutton(master,text="Amazon",padx = 20,fg="white",bg="#343434",variable=v,value=3,selectcolor="#343434").place(x=100,y=100)
Radiobutton(master,text="Flipkart",padx = 20,fg="white",bg="#343434",variable=v,value=4,selectcolor="#343434").place(x=100,y=130)


master.mainloop()


