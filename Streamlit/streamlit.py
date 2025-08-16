# Streamlit Library
import streamlit as st

# Main Library
import numpy as np 
import pandas as pd

# Visualization Library
import seaborn as sns
import matplotlib.pyplot as plt


# Page Config
st.set_page_config(layout='wide')

st.title("Dashboard of Weather Australia using Streamlit")

df = pd.read_csv("../Dataset/cleaned_weatherAUS.csv")

# Columns
col1, col2 = st.columns([0.5, 0.5], gap="medium")

with col1:
    st.info("Rain Tomorrow Countplot")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(df, x="RainTomorrow", hue="RainTomorrow")
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    st.pyplot(fig)

with col2:
    st.info("Rain Today Countplot")

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(df, x="RainToday", hue="RainToday")
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    st.pyplot(fig)

col1, col2 = st.columns([0.5, 0.5], gap="medium")

with col1:
    fig, ax = plt.subplots(figsize=(8, 4))
    df_heatmap = df[["MinTemp", "MaxTemp", "Rainfall", "Evaporation", "Sunshine"]].corr()
    sns.heatmap(data=df_heatmap, annot=True)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    st.pyplot(fig)