import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
x_axis = st.selectbox("Select the data for the x-axis", ("GDP","Happiness", "Generosity"))
y_axis= st.selectbox("Select the data for the y-axis", ("GDP","Happiness", "Generosity"))

st.subheader(f"{x_axis} and {y_axis}")

data = pd.read_csv('happy.csv')
data = data.rename(columns={"gdp":"GDP", "happiness":"Happiness","generosity":"Generosity"})

figure = px.scatter(x=data[x_axis], y=data[y_axis], labels={"x":x_axis, "y":y_axis})

st.plotly_chart(figure)