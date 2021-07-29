# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


icon = Image.open('icon.png')
st.set_page_config(
     page_title="QSS",
     page_icon=icon,
     layout="wide",
     initial_sidebar_state="expanded",
 )
icon2= Image.open('logo.png')
st.sidebar.image(icon2)
icon1= Image.open('banner.jpg')
st.image(icon1)
st.header('Welcome')
saydbar=st.sidebar.selectbox('Select Page', [1,2,3])


read_fayl=pd.read_csv('loan_prediction.csv')
def page1():
    
    st.dataframe(read_fayl)
    st.text('First Page')
def page2():
    fig = plt.figure(figsize =(10, 7))
    sns.countplot(read_fayl['Gender'])
    st.pyplot(fig)
    
    snss = plt.figure(figsize =(10, 7))
    sns.heatmap(read_fayl.isnull(),yticklabels=False)
    st.pyplot(snss)
    st.text('Second Page')
def page3():
    pltt=plt.figure(figsize=(12, 7))
    sns.set_style('darkgrid')
    sns.boxplot(x='ApplicantIncome',y='Dependents',data=read_fayl,palette='Dark2').set_title('Dependents')
    st.pyplot(pltt)
    
    plt1=plt.figure(figsize=(12, 7))
    sns.distplot(read_fayl['ApplicantIncome'].dropna(), kde=True, bins=30, color='Green').set_title('distribition_of_app')
    st.pyplot(plt1)
    st.text('Third Page')

if saydbar == 1:
    page1()
elif saydbar == 2:
    page2()
elif saydbar == 3:
    page3()
    
