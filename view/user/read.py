import pandas as pd
import streamlit as st
import sys
import os 
view_dir=os.path.dirname(__file__)
controller_path=os.path.join(view_dir,'..','controller')
sys.path.append(controller_path)
from user import view_all_data,view_user,view_only_names

def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id','email','fname','lname','photoURL','password'])
    with st.expander("View all Users"):
        st.dataframe(df)

def read_user():
    list_of_users = [i[0] for i in view_only_names()]
    selected_user = st.selectbox("Select your email", list_of_users)
    selected_result = view_user(selected_user)
    df = pd.DataFrame(selected_result, columns=['id','email','fname','lname','photoURL','password'])
    with st.expander("View your details"):
        st.dataframe(df)