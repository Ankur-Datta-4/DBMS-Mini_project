import datetime

import pandas as pd
import streamlit as st
import sys
import os 
view_dir=os.path.dirname(__file__)
controller_path=os.path.join(view_dir,'..',"..",'controller')
sys.path.append(controller_path)
# from train import view_all_data, view_only_train_names, get_details, update_train
from user import view_all_data, view_only_names, view_user
from user import update_user as update_user_c

def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id','email','fname','lname','photoURL','password'])
    with st.expander("Current Users"):
        st.dataframe(df)
    list_of_users = [i[0] for i in view_only_names()]
    selected_user = st.selectbox("User To Edit", list_of_users)
    selected_result = view_user(selected_user)
    # st.write(selected_result)
    if selected_result:
        id = selected_result[0][0]
        email = selected_result[0][1]
        fname = selected_result[0][2]
        lname = selected_result[0][3]
        photoURL = selected_result[0][4]
        password = selected_result[0][5]

    # Layout of Create
    col1, col2 = st.columns(2)

    with col1:
        user_email = st.text_input("user Email : ",email)
        user_fname = st.text_input("user FName : ",fname)
        user_lname = st.text_input("user LName : ",lname)
    with col2:
        new_photoURL = st.text_input("user photoURL : ",photoURL)
        new_password = st.text_input("user password : ",password)
        
    if st.button("Update User"):
        update_user(user_email,user_fname,user_lname,new_photoURL,new_password,email)
        st.success("Successfully updated:: {} to ::{}".format(fname, user_fname))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['id','email','fname','lname','photoURL','password'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_user():
    
    list_of_users = [i[0] for i in view_only_names()]
    selected_user = st.selectbox("User To Edit", list_of_users)
    selected_result = view_user(selected_user)
    # st.write(selected_result)
    if selected_result:
        id = selected_result[0][0]
        email = selected_result[0][1]
        fname = selected_result[0][2]
        lname = selected_result[0][3]
        photoURL = selected_result[0][4]
        password = selected_result[0][5]

    # Layout of Create
    col1, col2 = st.columns(2)

    with col1:
        user_email = st.text_input("user Email : ",email)
        user_fname = st.text_input("user FName : ",fname)
        user_lname = st.text_input("user LName : ",lname)
    with col2:
        new_photoURL = st.text_input("user photoURL : ",photoURL)
        new_password = st.text_input("user password : ",password)
        
    if st.button("Update User"):
        update_user_c(user_email,user_fname,user_lname,new_photoURL,new_password,email)
        st.success("Successfully updated:: {} to ::{}".format(fname, user_fname))

    result2 = view_user(user_email)
    df2 = pd.DataFrame(result2, columns=['id','email','fname','lname','photoURL','password'])
    with st.expander("Updated data"):
        st.dataframe(df2)