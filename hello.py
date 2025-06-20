import streamlit as st
import pandas as pd
import numpy as np

st.write("hello world")
x = st.text_input("movie", "star wars")

if st.button("click"):
    st.write(f"your favorite movie is `{x}`")

data = pd.read_csv("movies.csv")
st.write(data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.bar_chart(chart_data)
