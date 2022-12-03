import streamlit as st
import sys
import os 
import pandas as pd

view_dir=os.path.dirname(__file__)
controller_path=os.path.join(view_dir,'..','controller')
sys.path.append(controller_path)
from subscription import create_subscription,view_user_subscriptions
from user import view_only_names

def read():
    list_of_users = [i[0] for i in view_only_names()]
    email = st.selectbox("User Email", list_of_users,key="user-email")    
    with st.expander("View Subscriptions"):
        result=view_user_subscriptions(email)   
        df = pd.DataFrame(result, columns=['startsAt','userId','subscriptionId','Tier_name','Tier_price','validity_days','createdAt'])
        st.dataframe(df)