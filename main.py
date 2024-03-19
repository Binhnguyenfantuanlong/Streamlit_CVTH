import streamlit as st
import time
st.button(label="Login")
if st.button("Click me"):
  st.balloons()
p = st.progress(0)
for i in range(101):
  p.progress(0+i)
  time.sleep(0.1)

st.balloons()
