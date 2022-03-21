import streamlit as st
import joblib
mode1=joblib.load('spam-ham')
st.title('SPAM HAM CLASSIFIER')
ip=st.text_input('Enter your message')
op=mode1.predict([ip])
if st.button ('Predict'):
   st.title(op[0])
           
       
