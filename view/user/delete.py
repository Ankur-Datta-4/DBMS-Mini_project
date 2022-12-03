import pandas as pd
import streamlit as st
import sys
import os 
view_dir=os.path.dirname(__file__)
controller_path=os.path.join(view_dir,'..',"..",'controller')
sys.path.append(controller_path)
from user import view_only_names,delete_user
def delete():
    all_users=[i[0] for i in view_only_names()]
    selected_user=st.selectbox("Select User",all_users)
    if st.button('Delete user?'):
        delete_user(selected_user)