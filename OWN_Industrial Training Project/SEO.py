import os
import tkinter as tk
from tkinter import *
from tkinter import  ttk
from tkinter import Frame
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import bs4
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import pandas as pd
import numpy as np
import requests
import selenium
from selenium import webdriver
import csv
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer, word_tokenize, sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import lxml
import string
from string import punctuation
import random
import collections
from collections import Counter
import termcolor
from termcolor import colored

win = tk.Tk()
win.geometry('1200x600')
win.resizable(width=False ,height=False)

copyWrite = tk.Label(win, text = '© 2019 Shivam verma')
copyWrite.configure(bg = 'black', fg='white')
copyWrite.grid()
copyWrite.place(x=600,y=580, anchor = "center")

win.title('SEO SearchEngineOptimization !!')
win.configure(bg='black')

canvas = Canvas(width = 1200, height = 600, bg = 'black' )
canvas.grid()

photo = PhotoImage(file='D:\\Python exercise\\pythons projects\\OWN_Industrial Training Project\\pic.PNG')
canvas.create_image(2,2, image = photo, anchor=NW)

inBox = tk.Label(win, text='Enter URL : ', font=(16) )
inBox.configure(bg='black',fg='white') 
inBox.grid()
inBox.place(x = 255 ,y = 500, anchor = "center")

inPut = ttk.Entry(win, width = 60, font=(16))
inPut.grid()
inPut.place(x = 645, y = 500, anchor ="center")

def onclick():
    print(inPut)
    
  

btn = ttk.Button(win, text="Submit", command = onclick )
btn.grid()
btn.place(x=1025,y=500, anchor='center')


# create a new Firefox session
binary = FirefoxBinary(r"C:\\Program Files\\Mozilla Firefox\\firefox.exe")
caps = DesiredCapabilities.FIREFOX.copy()
caps['marionette'] = True
driver=webdriver.Firefox(firefox_binary=binary,capabilities=caps,executable_path="C:\\Users\\Dell\\AppData\Local\\Programs\\Python\\Python37-32\\geckodriver-v0.24.0-win64\\geckodriver.exe")
driver.implicitly_wait(30)
driver.get(inPut)
#dataset = pd.read_csv('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python37-32\\papers1.csv','wb',error_bad_lines=False,delimiter = '\t , \n',engine='python')
#dataset.head()

#finding keywords
bsurl=urlopen(inPut)
soup=BeautifulSoup(bsurl, "lxml")
keywords= soup.find("meta",property="og:keywords")
print(colored("Keywords from the web page are:") +keywords["content"] if keywords else "No keywords found")
#telling driver to click a link
python_button = driver.find_element_by_link_text(input("Enter the link text you want to find:")) #FHSU
python_button.click()
print("Link Text found and clicked")
#stopwords counter
word = re.sub("[^a-zA-Z]"," ",soup.getText())
#extract words
words = word_tokenize(word)
#remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if not w in stop_words]
a = Counter([x.lower() for y in filtered_words for x in y.split()])
b = (a.most_common())
makeaframe = pd.DataFrame(b)
makeaframe.columns = ['Words', 'Frequency']
makeaframe.head()
print("Stopwords found and removed:")
print(makeaframe)
#word counter

# We get the words within paragrphs
text_p = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))

# We get the words within divs
text_div = (''.join(s.findAll(text=True))for s in soup.findAll('div'))
c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))

# We sum the two countesr and get a list with words count from most to less common
total = c_div + c_p
print("10 most common words are: ")
print(total.most_common(10))
#Selenium hands the page source to Beautiful Soup
soup_level1=BeautifulSoup(driver.page_source, 'lxml')
x = 0 #counter
#data=[driver.find_element_by_link_text("Older Posts"),'driver.find_element_by_link_text("Newer Posts")]
while x>=0:
    x+=1
#Beautiful Soup finds Title links on the agency page and the loop begins
    if x%2==0 and x%3!=0:
        for link in soup_level1.find_all('a',id=re.compile("Blog1_blog-pager-older-link")):
            python_button =driver.find_element_by_link_text("Older Posts") #FHSU
            python_button.click()
            print("Link to Older Posts clicked")
            if python_button==False:
                python_button=driver.find_element_by_link_text("Newer Posts")
                python_button.click()
                print("Link to Newer Posts clicked because start of the file reached")
        continue;
       
    elif x%3==0 and x%2!=0:
        for link in soup_level1.find_all('a',id=re.compile("Blog1_blog-pager-newer-link")):
            python_button =driver.find_element_by_link_text("Newer Posts") #FHSU
            python_button.click()
            print("Link to Newer Posts clicked")
        continue;
       #increment the counter variable before starting the loop over
       
    elif x%2==0 and x%3==0:
        driver.execute_script("window.history.go(-1)")
        print("Previous Page")
        continue;
       
    else:
        python_button=driver.find_element_by_link_text(input("Enter link text: "))
        python_button.click()
        print("Entred link clicked")
    continue;



win.mainloop() 
