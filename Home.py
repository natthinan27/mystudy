import json
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="การวิเคราะห์พฤติกรรมผู้บริโภคโดยการจัดกลุ่มแบบเคมีน",
    page_icon= ":bar_chart:",
)
html_1 = """
<div style="background-color:#6A5683;padding:5px;border-radius:5px;border-bottom: 5px solid #ffffff;border-top: 5px solid #ffffff;">
<center><h4>การวิเคราะห์พฤติกรรมผู้บริโภคโดยการจัดกลุ่มแบบเคมีน</h4><h5>Analyzes Consumer Behavior by K-means clustering</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

html_2 = """
<center><h5>บทคัดย่อ</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

html_3 = """
<div style="background-color:#6A5683;padding:15px;border-radius:1px 1px 1px 1px;border-style:'solid';border-color:black">
<center><h5>วัตถุประสงค์ของงานวิจัยนี้ คือ เพื่อช่วยธุรกิจหรือองค์กรในการทำให้เข้าใจลึกซึ้งเกี่ยวกับลูกค้าและตลาดของพวกเขา เพื่อให้สามารถดำเนินกิจการได้อย่างมีประสิทธิภาพมากยิ่งขึ้น นอกจากนี้การวิเคราะห์พฤติกรรมผู้บริโภคช่วยในการทำความเข้าใจถึงความต้องการของลูกค้าและที่สำคัญที่สุดในการพัฒนาผลิตภัณฑ์หรือบริการที่ตอบสนองต่อความต้องการนี้ ดังนั้นการวิเคราะห์พฤติกรรมผู้บริโภคเป็นเครื่องมือที่มีประโยชน์ในการทำให้ธุรกิจทราบถึงทิศทางที่เหมาะสมที่สุดในการพัฒนาและเติบโตขึ้นไปในอนาคต จึงได้ทำการทดลองการจัดกลุ่มแบบเคมีน กับชุดข้อมูลConsumer Behavior and Shopping Habits Datasetข้อมูลประกอบด้วย 1,000 แถว18 คอลัมน์ 
ผลการทดลอง วิธีการหาค่า Silhouette Score และ หาค่า Calinski-Harabasz Score ให้ประสิทธิภาพสูงสุดจะได้ค่าจะเห็นได้ว่า ค่า Silhouette Score ที่ได้คือ0.5368227965812387และ ค่า Calinski-Harabasz Score ที่ได้คือ 503.04653062320193
สรุปผลได้ว่า การจัดกลุ่มมีความเหมาะสมและมีความคล้ายคลึงภายในกลุ่มมาก และความแตกต่างระหว่างกลุ่มน้อย สามารถใช้ผลลัพธ์นี้เพื่อทำนายและวิเคราะห์ลักษณะของกลุ่มที่ได้จากการจัดกลุ่ม k-means clustering ได้
</h5></center>
</div>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")

html_4 = """
<center><h5>Abstract</h5></center>
</div>
"""
st.markdown(html_4, unsafe_allow_html=True)
st.markdown("")

html_5 = """
<div style="background-color:#433A4A;padding:15px;border-radius:1px 1px 1px 1px;border-style:'solid';border-color:black">
<center><h5>Abstract content The purpose of this research is to help businesses or organizations gain a deeper understanding of their customers and markets. In order to be able to conduct business more efficiently Moreover, consumer behavior analysis helps in understanding customer needs and most importantly in developing products or services that satisfy this need. Therefore, consumer behavior analysis is a useful tool to inform businesses about the most appropriate direction to develop and grow in the future. Therefore, a chemical grouping experiment was conducted. With the Consumer Behavior and Shopping Habits Dataset, the data consists of 1,000 rows and 18 columns.
Results of the experiment: How to find the Silhouette Score and find the Calinski-Harabasz Score for the highest efficiency. It can be seen that the Silhouette Score value obtained is 0.5368227965812387 and the Calinski-Harabasz Score value obtained is 503.04653062320193.
The results concluded that the grouping was appropriate and there were many similarities within the groups. and differences between groups This result can be used to predict and analyze the characteristics of clusters obtained from k-means clustering.
</h5></center>
</div>
</div>
"""
st.markdown(html_5, unsafe_allow_html=True)
st.markdown("")

