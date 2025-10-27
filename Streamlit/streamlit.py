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
    ax.legend(title='', ncol=2)
    st.pyplot(fig)

with col2:
    st.info("Rain Today Countplot")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(df, x="RainToday", hue="RainToday")
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    ax.legend(title='', ncol=2)
    st.pyplot(fig)

col1, col2 = st.columns([0.5, 0.5], gap="medium")

with col1:
    st.info("Weather Count Plot")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(df, x="WindGustDir", hue="RainTomorrow")
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    ax.legend(title='', ncol=2)
    st.pyplot(fig)

with col2:
    st.info("Weather Bar Plot")
    wgd = df.groupby("WindGustDir")["RainTomorrow"].count()
    wgd = wgd.sort_values(ascending=False)
    df_wgd = pd.DataFrame(wgd).reset_index()
    
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(df_wgd, x="WindGustDir", y="RainTomorrow")
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    # ax.legend(title='', ncol=2)
    st.pyplot(fig)

col1, col2 = st.columns([0.5, 0.5], gap="medium")

with col1:
    st.info("Weather Heatmap 1")
    fig, ax = plt.subplots(figsize=(8, 4))
    df_heatmap = df[["MinTemp", "MaxTemp", "Rainfall", "Evaporation", "Sunshine"]].corr()
    sns.heatmap(data=df_heatmap, annot=True)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    st.pyplot(fig)

with col2:
    st.info("Weather Heatmap 2")
    fig, ax = plt.subplots(figsize=(8, 4))
    df_heatmap = df[["Humidity9am", "Pressure9am", "Cloud9am", "Temp9am"]].corr()
    sns.heatmap(data=df_heatmap, annot=True)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    st.pyplot(fig)

col1, col2 = st.columns([0.5, 0.5], gap="medium")

with col1:
    st.info("Weather Group Bar Plot 1")
    fig, ax = plt.subplots(figsize=(8, 4))
    df_location = df.groupby("Location")[["MinTemp", "MaxTemp", "Rainfall"]].mean().sort_values(by='Rainfall', ascending=False).reset_index().head(5)
    df_location = np.round(df_location, decimals=1)
    df_melt = pd.melt(df_location, id_vars=['Location'], value_vars=['MinTemp', 'MaxTemp', 'Rainfall'])
    sns.barplot(data=df_melt, x="Location", y="value", hue="variable")
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    ax.legend(title='', ncol=3)
    st.pyplot(fig)

with col2:
    st.info("Weather Group Bar Plot 2")
    fig, ax = plt.subplots(figsize=(8, 4))
    df_location2 = df.groupby("Location")[["WindSpeed9am", "Humidity9am", "Cloud9am"]].mean().sort_values(by='Cloud9am', ascending=False).reset_index().head(5)
    df_location2 = np.round(df_location2, decimals=2)
    df_melt2 = pd.melt(df_location2, id_vars=['Location'], value_vars=['WindSpeed9am', 'Humidity9am', 'Cloud9am'])
    sns.barplot(data=df_melt2, x="Location", y="value", hue="variable")
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    ax.legend(title='', ncol=3)
    st.pyplot(fig)

col1, col2 = st.columns([0.5, 0.5], gap="medium")

with col1:
    st.info("Weather Scatter 1")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(data=df, x="WindGustSpeed", y="Pressure3pm", hue="Pressure3pm")
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    ax.legend(title='', ncol=2)
    st.pyplot(fig, use_container_width=True)

with col2:
    st.info("Weather Scatter 2")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(data=df, x="WindSpeed9am", y="WindSpeed3pm", hue="Humidity9am")
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    ax.legend(title='', ncol=6)
    st.pyplot(fig, use_container_width=True)

col1, col2 = st.columns([0.5, 0.5], gap="medium")

with col1:
    st.info("Weather Violin")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.violinplot(data=df_heatmap, bw_adjust=.5, cut=1, linewidth=1, palette="Set3")
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    ax.legend(title='', ncol=2)
    st.pyplot(fig, use_container_width=True)

with col2:
    st.info("Weather Boxen")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxenplot(data=df, x="Temp3pm", y="WindGustDir", width_method="linear")
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('')
    ax.grid(True)
    ax.legend(title='', ncol=2)
    st.pyplot(fig, use_container_width=True)
