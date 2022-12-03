import streamlit as st
import sys
import os 
view_dir=os.path.dirname(__file__)
controller_path=os.path.join(view_dir,'..',"..",'controller')
sys.path.append(controller_path)
from user import create_user
# from database import add_data

def create():
    col1, col2 = st.columns(2)
    with col1:
        user_email = st.text_input("user Email : ")
        user_fname = st.text_input("user FName : ")
        user_lname = st.text_input("user LName : ")
    with col2:
        photoURL = st.text_input("user photoURL : ")
        password = st.text_input("user password : ")
        
    if st.button("Add A New user"):
        create_user(user_email,password,user_fname,user_lname,photoURL)
        st.success("Successfully added user: {}".format(user_fname))