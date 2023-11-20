import json
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="การวิเคราะห์พฤติกรรมผู้บริโภคโดยการจัดกลุ่มแบบเคมีน",
    page_icon= ":bar_chart:",
)
html_1 = """
<div style="background-color:#433A4A;padding:5px;border-radius:5px;border-bottom: 5px solid #ffffff;border-top: 5px solid #ffffff;">
<center><h4>การวิเคราะห์พฤติกรรมผู้บริโภคโดยการจัดกลุ่มแบบเคมีน</h4><h5>Analyzes Consumer Behavior by K-means clustering</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")


html_2 = """
<div style="background-color:#32174d;padding:1px;border-radius:1px 1px 1px 1px;border-style:'solid';border-color:black">
<center><h5>การวิเคราะห์พฤติกรรมผู้บริโภคโดยการจัดกลุ่มแบบเคมีน</h5></center>
<center><h5>Analyzes Consumer Behavior by K-means clustering</h5></center>
</div>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

