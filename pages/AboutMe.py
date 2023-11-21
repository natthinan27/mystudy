import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.header("")
col1, col2, col3 = st.columns([1.5, 6, 1])

with col1:
    st.write("") 

with col2:
    st.image("./img/s3.jpg")

with col3:
    st.write("")



html_8 = """
<div style="background-color:#6e91df;padding:10px;border-radius:10px 10px 10px 10px;border-style:'solid';border-color:black">
<center><h5>นางสาวณัฐินันท์ เข็มทอง 644285002 64/44</h5></center>
</div>
"""

st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

